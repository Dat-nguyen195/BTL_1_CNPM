from pathlib import Path
import ast,copy,json,sys,types,importlib.util,datetime
ROOT=Path.cwd(); sys.path.insert(0,str(ROOT/'src'))
from core.scheduler import SmartChargingScheduler,ChargingRequest
from core.simulator import HubEventSimulator
DATA=json.loads((ROOT/'src/data/mock_hubs.json').read_text())
results=[]
def record(name,detail): results.append({'probe':name,'observed':detail});print(name,detail)
class UI:
 def __init__(self):self.session_state={};self.click=None;self.dest=None;self.minutes=25;self.pin='123456';self.form_name=None
 def __enter__(self):return self
 def __exit__(self,*a):pass
 def columns(self,n):return [self]*(n if isinstance(n,int) else len(n))
 def tabs(self,labels):return [self]*len(labels)
 def form(self,name,**k):self.form_name=name;return self
 def expander(self,*a,**k):return self
 def button(self,label,**k):return k.get('key')==self.click
 def form_submit_button(self,*a,**k):return self.form_name=='book_charge_form'
 def selectbox(self,label,options,**k):return self.dest if label=='Hub trả xe:' and self.dest else options[k.get('index',0)]
 def radio(self,label,options,**k):return options[0]
 def text_input(self,label,*a,**k):return self.pin if k.get('key')=='pu_pin' else k.get('value','')
 def text_area(self,label,value='',*,placeholder=None):return value
 def number_input(self,*a,**k):return self.minutes
 def slider(self,*a,**k):return 45
 def __getattr__(self,name):return lambda *a,**k:None
ui=UI()
def module(path):
 tree=ast.parse(path.read_text());tree.body=[n for n in tree.body if not(isinstance(n,ast.Import) and any(a.name=='streamlit' for a in n.names))]
 ns={'st':ui};exec(compile(tree,str(path),'exec'),ns);return ns
ss1=module(ROOT/'src/components/student_booking.py')
def setup(status='RESERVED',wallet=450000):
 ui.session_state={'hubs':copy.deepcopy(DATA),'bookings':[],'current_user':{'name':'test','student_id':'test','wallet_balance':wallet,'locked_balance':50000}}
 h=ui.session_state['hubs'][0];v=h['current_vehicles'][0];v['status']='reserved' if status=='RESERVED' else 'in_use'
 b={'vehicle_id':v['vehicle_id'],'hub_origin':h['name'],'hub_origin_id':h['hub_id'],'status':status,'pin_code':'123456','deposit':50000,'discount':0,'booked_at':'00:00:00 01/01/2000','picked_up_at':'00:00:00 01/01/2000'};ui.session_state['bookings'].append(b);return h,b
h,b=setup();ui.click='pu_confirm';ss1['_tab_pickup']();record('expired_pin_accepted',{'booking_status':b['status'],'booked_at':b['booked_at']})
h,b=setup();ui.click='cn_confirm';ss1['_tab_cancel']();record('expired_cancel_full_refund',{'wallet':ui.session_state['current_user']['wallet_balance'],'cost':b['total_cost']})
h,b=setup('IN_USE',1000);ui.click='rt_confirm';ui.dest=h['name'];ui.minutes=300;before=h['available_slots'];ss1['_tab_return']();record('same_hub_return_unpaid',{'slots_before':before,'slots_after':h['available_slots'],'charge':b['total_cost'],'wallet':ui.session_state['current_user']['wallet_balance'],'booking':b['status']})
ss2=module(ROOT/'src/components/personal_ev.py');ui.session_state={'hubs':copy.deepcopy(DATA),'personal_evs':[{'ev_id':'PEV-TEST','owner':'test','mssv':'1','plate':'TEST','type':'bike','brand':'test','battery_kwh':2,'registered_at':'test','status':'registered'}]};ui.click=None;ui.minutes=25;ss2['render']();ss2['render']();h=ui.session_state['hubs'][0];record('duplicate_personal_ev_booking',{'same_id_occurrences':sum(v['vehicle_id']=='PEV-TEST' for v in h['current_vehicles']),'slots':h['available_slots'],'private_vehicle_status':ui.session_state['personal_evs'][0]['status']})
ss4=module(ROOT/'src/components/dispatch_incident.py');tree=ast.parse((ROOT/'src/components/dispatch_incident.py').read_text());node=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and n.lineno==92)
try:exec(compile(ast.Module(body=[node],type_ignores=[]),'SS4-call','exec'),{'st':ui})
except TypeError as e:record('ss4_text_area',str(e))
q=SmartChargingScheduler()
for soc,book in [(5,False),(30,False),(30,True)]:
 req=ChargingRequest('test','HUB-001',soc,book);q.add_request(req);record('scheduler_score',{'soc':soc,'booking':book,'score':req.priority_score})
q.add_request(ChargingRequest('test','HUB-001',30));record('scheduler_duplicate_ids',q.queue_length)
baseline=copy.deepcopy(DATA);modified,log=HubEventSimulator(DATA).simulate_port_failure('HUB-004',3);h=modified[3];record('port_failure_3',{'original_unchanged':DATA==baseline,'ports':h['charging_ports'],'hub_status':h.get('status'),'waiting':sum(v['status']=='waiting' for v in h['current_vehicles'])})
synthetic=copy.deepcopy(DATA);h=synthetic[0];h['charging_ports']={'total':2,'available':0};h['current_vehicles']=[{'vehicle_id':'X','type':'bike','battery_soc':10,'status':'charging'},{'vehicle_id':'Y','type':'bike','battery_soc':20,'status':'charging'}];new,log=HubEventSimulator(synthetic).simulate_port_failure('HUB-001',2);record('all_busy_ports_failure',{'charging_after':sum(v['status']=='charging' for v in new[0]['current_vehicles']),'log':log})
new,log=HubEventSimulator(DATA).simulate_metro_surge('HUB-002',20);record('metro_surge_copy',{'original_unchanged':DATA==baseline,'slots_after':new[1]['available_slots'],'added_vehicles':len(new[1]['current_vehicles'])-len(DATA[1]['current_vehicles'])})
for f in ('sim_demand.py','sim_infrastructure.py'):
 tree=ast.parse((ROOT/'src/components'/f).read_text());found=[]
 for n in ast.walk(tree):
  if isinstance(n,ast.If) and isinstance(n.test,ast.Call) and isinstance(n.test.func,ast.Attribute) and n.test.func.attr=='button':
   nested=[x.lineno for x in ast.walk(ast.Module(body=n.body,type_ignores=[])) if isinstance(x,ast.Call) and isinstance(x.func,ast.Attribute) and x.func.attr=='button'];
   if nested:found.append({'outer':n.lineno,'nested_button_lines':nested})
 record('nested_buttons_'+f,found)
Path('/tmp/emobility-audit/probes.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
