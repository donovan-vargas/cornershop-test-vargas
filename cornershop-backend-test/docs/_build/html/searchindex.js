Search.setIndex({docnames:["backend_test","backend_test.utils","employees","employees.migrations","employees.utils","gunicorn_config","index","lunch","lunch.migrations","lunch.tests","lunch.utils","manage","modules"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.todo":1,"sphinx.ext.viewcode":1,sphinx:55},filenames:["backend_test.rst","backend_test.utils.rst","employees.rst","employees.migrations.rst","employees.utils.rst","gunicorn_config.rst","index.rst","lunch.rst","lunch.migrations.rst","lunch.tests.rst","lunch.utils.rst","manage.rst","modules.rst"],objects:{"":{backend_test:[0,0,0,"-"],employees:[2,0,0,"-"],gunicorn_config:[5,0,0,"-"],lunch:[7,0,0,"-"],manage:[11,0,0,"-"]},"backend_test.celery":{CelerySettings:[0,1,1,""]},"backend_test.celery.CelerySettings":{BROKER_CONNECTION_MAX_RETRIES:[0,2,1,""],BROKER_HEARTBEAT:[0,2,1,""],BROKER_POOL_LIMIT:[0,2,1,""],BROKER_URL:[0,2,1,""],CELERYD_HIJACK_ROOT_LOGGER:[0,2,1,""],CELERYD_POOL_RESTARTS:[0,2,1,""],CELERYD_TASK_SOFT_TIME_LIMIT:[0,2,1,""],CELERYD_TASK_TIME_LIMIT:[0,2,1,""],CELERYD_WORKER_LOST_WAIT:[0,2,1,""],CELERY_ACCEPT_CONTENT:[0,2,1,""],CELERY_ACKS_LATE:[0,2,1,""],CELERY_ALWAYS_EAGER:[0,2,1,""],CELERY_DEFAULT_EXCHANGE:[0,2,1,""],CELERY_DEFAULT_QUEUE:[0,2,1,""],CELERY_DEFAULT_ROUTING_KEY:[0,2,1,""],CELERY_EAGER_PROPAGATES_EXCEPTIONS:[0,2,1,""],CELERY_ENABLE_UTC:[0,2,1,""],CELERY_IGNORE_RESULT:[0,2,1,""],CELERY_RESULT_BACKEND:[0,2,1,""],CELERY_RESULT_SERIALIZER:[0,2,1,""],CELERY_STORE_ERRORS_EVEN_IF_IGNORED:[0,2,1,""],CELERY_TASK_REJECT_ON_WORKER_LOST:[0,2,1,""],CELERY_TASK_RESULT_EXPIRES:[0,2,1,""],CELERY_TASK_SERIALIZER:[0,2,1,""],CELERY_TIMEZONE:[0,2,1,""]},"backend_test.envtools":{getenv:[0,3,1,""]},"backend_test.logging_formatter":{VerboseFluentRecordFormatter:[0,1,1,""]},"backend_test.logging_formatter.VerboseFluentRecordFormatter":{encoder:[0,2,1,""],encoder_class:[0,2,1,""],format:[0,4,1,""],json_encode:[0,4,1,""]},"backend_test.middleware":{HeaderNoCacheMiddleware:[0,1,1,""],HealthCheckAwareSessionMiddleware:[0,1,1,""]},"backend_test.middleware.HealthCheckAwareSessionMiddleware":{process_request:[0,4,1,""]},"backend_test.urls":{path:[0,3,1,""]},"backend_test.utils":{healthz:[1,0,0,"-"]},"backend_test.utils.healthz":{healthz:[1,3,1,""]},"employees.apps":{EmployeesConfig:[2,1,1,""]},"employees.apps.EmployeesConfig":{name:[2,2,1,""]},"employees.migrations":{"0001_initial":[3,0,0,"-"]},"employees.migrations.0001_initial":{Migration:[3,1,1,""]},"employees.migrations.0001_initial.Migration":{dependencies:[3,2,1,""],initial:[3,2,1,""],operations:[3,2,1,""]},"employees.models":{Employee:[2,1,1,""]},"employees.models.Employee":{DoesNotExist:[2,5,1,""],MultipleObjectsReturned:[2,5,1,""],active:[2,2,1,""],created:[2,2,1,""],employee:[2,2,1,""],employee_id:[2,2,1,""],get_next_by_created:[2,4,1,""],get_next_by_modified:[2,4,1,""],get_previous_by_created:[2,4,1,""],get_previous_by_modified:[2,4,1,""],id:[2,2,1,""],modified:[2,2,1,""],objects:[2,2,1,""],order_employee:[2,2,1,""],unique_id:[2,2,1,""]},"employees.utils":{install_users:[4,0,0,"-"]},"employees.utils.install_users":{create_employees:[4,3,1,""],create_nora_user:[4,3,1,""]},"gunicorn_config.MemoryWatch":{memory_usage:[5,4,1,""],run:[5,4,1,""]},"lunch.apps":{LunchConfig:[7,1,1,""]},"lunch.apps.LunchConfig":{name:[7,2,1,""]},"lunch.forms":{MenuForm:[7,1,1,""],OrderForm:[7,1,1,""]},"lunch.forms.MenuForm":{Meta:[7,1,1,""],base_fields:[7,2,1,""],clean:[7,4,1,""],declared_fields:[7,2,1,""],media:[7,2,1,""]},"lunch.forms.MenuForm.Meta":{fields:[7,2,1,""],model:[7,2,1,""]},"lunch.forms.OrderForm":{Meta:[7,1,1,""],base_fields:[7,2,1,""],clean:[7,4,1,""],declared_fields:[7,2,1,""],media:[7,2,1,""]},"lunch.forms.OrderForm.Meta":{fields:[7,2,1,""],model:[7,2,1,""]},"lunch.migrations":{"0001_initial":[8,0,0,"-"],"0002_auto_20210702_1647":[8,0,0,"-"],"0003_menu_unique_id":[8,0,0,"-"]},"lunch.migrations.0001_initial":{Migration:[8,1,1,""]},"lunch.migrations.0001_initial.Migration":{dependencies:[8,2,1,""],initial:[8,2,1,""],operations:[8,2,1,""]},"lunch.migrations.0002_auto_20210702_1647":{Migration:[8,1,1,""]},"lunch.migrations.0002_auto_20210702_1647.Migration":{dependencies:[8,2,1,""],operations:[8,2,1,""]},"lunch.migrations.0003_menu_unique_id":{Migration:[8,1,1,""]},"lunch.migrations.0003_menu_unique_id.Migration":{dependencies:[8,2,1,""],operations:[8,2,1,""]},"lunch.models":{Menu:[7,1,1,""],MenuOptions:[7,1,1,""],Orders:[7,1,1,""]},"lunch.models.Menu":{DoesNotExist:[7,5,1,""],MultipleObjectsReturned:[7,5,1,""],active:[7,2,1,""],created:[7,2,1,""],date:[7,2,1,""],get_next_by_created:[7,4,1,""],get_next_by_date:[7,4,1,""],get_next_by_modified:[7,4,1,""],get_previous_by_created:[7,4,1,""],get_previous_by_date:[7,4,1,""],get_previous_by_modified:[7,4,1,""],id:[7,2,1,""],menu_option:[7,2,1,""],menu_user:[7,2,1,""],menu_user_id:[7,2,1,""],message:[7,2,1,""],modified:[7,2,1,""],name:[7,2,1,""],objects:[7,2,1,""],sent:[7,2,1,""],unique_id:[7,2,1,""]},"lunch.models.MenuOptions":{DoesNotExist:[7,5,1,""],MultipleObjectsReturned:[7,5,1,""],active:[7,2,1,""],created:[7,2,1,""],get_next_by_created:[7,4,1,""],get_next_by_modified:[7,4,1,""],get_previous_by_created:[7,4,1,""],get_previous_by_modified:[7,4,1,""],id:[7,2,1,""],menu:[7,2,1,""],menu_id:[7,2,1,""],modified:[7,2,1,""],objects:[7,2,1,""],option:[7,2,1,""],order_option:[7,2,1,""]},"lunch.models.Orders":{DoesNotExist:[7,5,1,""],MultipleObjectsReturned:[7,5,1,""],active:[7,2,1,""],created:[7,2,1,""],customizations:[7,2,1,""],employee:[7,2,1,""],employee_id:[7,2,1,""],get_next_by_created:[7,4,1,""],get_next_by_modified:[7,4,1,""],get_previous_by_created:[7,4,1,""],get_previous_by_modified:[7,4,1,""],id:[7,2,1,""],modified:[7,2,1,""],objects:[7,2,1,""],option:[7,2,1,""],option_id:[7,2,1,""]},"lunch.tasks":{setup_periodic_tasks:[7,3,1,""]},"lunch.tests":{test_forms:[9,0,0,"-"],test_models:[9,0,0,"-"],test_task:[9,0,0,"-"],test_views:[9,0,0,"-"]},"lunch.tests.test_forms":{MenuFormTestCase:[9,1,1,""],OrderFormTestCase:[9,1,1,""]},"lunch.tests.test_forms.MenuFormTestCase":{setUp:[9,4,1,""],test_date_form:[9,4,1,""],test_menu_form:[9,4,1,""],test_menu_form_required_date:[9,4,1,""],test_menu_form_required_name:[9,4,1,""]},"lunch.tests.test_forms.OrderFormTestCase":{setUp:[9,4,1,""],test_menu_form:[9,4,1,""]},"lunch.tests.test_models":{MenuOptionsTestCase:[9,1,1,""],MenuTestCase:[9,1,1,""],OrdersTestCase:[9,1,1,""]},"lunch.tests.test_models.MenuOptionsTestCase":{setUp:[9,4,1,""],test_menu:[9,4,1,""],test_name_max_length:[9,4,1,""]},"lunch.tests.test_models.MenuTestCase":{setUp:[9,4,1,""],test_menu:[9,4,1,""],test_message_max_length:[9,4,1,""],test_name_max_length:[9,4,1,""],test_sent:[9,4,1,""],test_uuid:[9,4,1,""],test_validate_date:[9,4,1,""]},"lunch.tests.test_models.OrdersTestCase":{setUp:[9,4,1,""],test_orders:[9,4,1,""]},"lunch.tests.test_task":{SendMenuTaskTestCase:[9,1,1,""],SendMessageSlack:[9,1,1,""]},"lunch.tests.test_task.SendMenuTaskTestCase":{setUp:[9,4,1,""],test_fail:[9,4,1,""],test_success:[9,4,1,""]},"lunch.tests.test_task.SendMessageSlack":{test_send_fail:[9,4,1,""],test_send_success:[9,4,1,""]},"lunch.tests.test_views":{MenuViewsTestCalls:[9,1,1,""]},"lunch.tests.test_views.MenuViewsTestCalls":{setUp:[9,4,1,""],test_call_view_deny_anonymous:[9,4,1,""],test_call_view_load:[9,4,1,""],test_call_view_permision:[9,4,1,""]},"lunch.urls":{path:[7,3,1,""]},"lunch.utils":{slack:[10,0,0,"-"]},"lunch.utils.slack":{send_message_slack:[10,3,1,""]},"lunch.views":{DetailMenuView:[7,1,1,""],LoginView:[7,1,1,""],LogoutView:[7,1,1,""],MenuCreateView:[7,1,1,""],MenuUpdateView:[7,1,1,""],OrderListView:[7,1,1,""],OrdersView:[7,1,1,""]},"lunch.views.DetailMenuView":{model:[7,2,1,""],slug_field:[7,2,1,""],slug_url_kwarg:[7,2,1,""],template_name:[7,2,1,""]},"lunch.views.LoginView":{dispatch:[7,4,1,""],form_class:[7,2,1,""],form_valid:[7,4,1,""],success_url:[7,2,1,""],template_name:[7,2,1,""]},"lunch.views.LogoutView":{get:[7,4,1,""],pattern_name:[7,2,1,""]},"lunch.views.MenuCreateView":{context_object_name:[7,2,1,""],dispatch:[7,4,1,""],form_class:[7,2,1,""],model:[7,2,1,""],post:[7,4,1,""],success_url:[7,2,1,""]},"lunch.views.MenuUpdateView":{context_object_name:[7,2,1,""],dispatch:[7,4,1,""],form_class:[7,2,1,""],model:[7,2,1,""],post:[7,4,1,""],success_url:[7,2,1,""]},"lunch.views.OrderListView":{context_object_name:[7,2,1,""],dispatch:[7,4,1,""],model:[7,2,1,""]},"lunch.views.OrdersView":{form_class:[7,2,1,""],get:[7,4,1,""],get_context_data:[7,4,1,""],model:[7,2,1,""],post:[7,4,1,""]},backend_test:{celery:[0,0,0,"-"],conftest:[0,0,0,"-"],envtools:[0,0,0,"-"],logging_formatter:[0,0,0,"-"],middleware:[0,0,0,"-"],settings:[0,0,0,"-"],urls:[0,0,0,"-"],utils:[1,0,0,"-"],wsgi:[0,0,0,"-"]},employees:{admin:[2,0,0,"-"],apps:[2,0,0,"-"],migrations:[3,0,0,"-"],models:[2,0,0,"-"],tests:[2,0,0,"-"],utils:[4,0,0,"-"],views:[2,0,0,"-"]},gunicorn_config:{MemoryWatch:[5,1,1,""],post_fork:[5,3,1,""],when_ready:[5,3,1,""]},lunch:{admin:[7,0,0,"-"],apps:[7,0,0,"-"],forms:[7,0,0,"-"],migrations:[8,0,0,"-"],models:[7,0,0,"-"],tasks:[7,0,0,"-"],tests:[9,0,0,"-"],urls:[7,0,0,"-"],utils:[10,0,0,"-"],views:[7,0,0,"-"]},manage:{main:[11,3,1,""]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","attribute","Python attribute"],"3":["py","function","Python function"],"4":["py","method","Python method"],"5":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:attribute","3":"py:function","4":"py:method","5":"py:exception"},terms:{"0001_initi":[2,7,12],"0002_auto_20210702_1647":[7,12],"0003_menu_unique_id":[7,12],"case":9,"class":[0,2,3,5,7,8,9],"default":0,"function":0,"import":0,"new":7,"return":[0,7,10],"super":4,"true":[0,2,3,7,8],"try":0,For:0,The:[0,5],__first__:[3,8],accessor:[2,7],activ:[2,3,5,7,8],add:[0,7,9],addfield:8,admin:[0,12],administr:11,alia:7,alterfield:8,altermodelopt:8,ani:[0,5],anoth:0,app:12,app_label:[3,8],app_modul:[2,7],app_nam:[2,7],appconfig:[2,7],append:0,appli:0,applic:0,arg:[1,2,5,7],argument:5,as_view:0,asert:9,attribut:0,auth:[3,7,8],authenticationform:7,auto_id:7,autofield:[3,8],backend_test:12,base:[0,2,3,5,7,8,9],base_field:7,befor:0,below:[2,7],blog:0,bool:0,booleanfield:[2,3,7,8],broker_connection_max_retri:0,broker_heartbeat:0,broker_pool_limit:0,broker_url:0,built:[2,7],call:0,callabl:[0,5],can:[7,8],can_create_menu:[7,8],can_edit_menu:[7,8],can_see_ord:[7,8],cant:9,carri:0,celeri:[7,9,12],celery_accept_cont:0,celery_acks_l:0,celery_always_eag:0,celery_default_exchang:0,celery_default_queu:0,celery_default_routing_kei:0,celery_eager_propagates_except:0,celery_enable_utc:0,celery_ignore_result:0,celery_result_backend:0,celery_result_seri:0,celery_store_errors_even_if_ignor:0,celery_task_reject_on_worker_lost:0,celery_task_result_expir:0,celery_task_seri:0,celery_timezon:0,celeryd_hijack_root_logg:0,celeryd_pool_restart:0,celeryd_task_soft_time_limit:0,celeryd_task_time_limit:0,celeryd_worker_lost_wait:0,celeryset:0,chanel:9,channel:10,charfield:[7,8],child:[2,7],children:[2,7],chile:7,clean:7,coalesc:0,code:7,com:0,command:11,comput:0,config:[0,2,7],configur:0,conftest:12,constructor:5,content:12,context:7,context_object_nam:7,contrib:[0,7],core:[2,7],correct:9,coupl:0,creat:[2,3,4,7,8,9],create_employe:4,create_forward_many_to_many_manag:[2,7],create_nora_us:4,createmodel:[3,8],createview:7,custom:[7,8],data:7,date:[2,7,8,9],datefield:[2,3,7,8],datetim:7,datetimefield:[2,3,7,8],declared_field:7,defer:[2,7],defin:[2,7],deleg:[2,7],delet:[2,7],depend:[3,8],deploy:0,detail:7,detailmenuview:7,detailview:7,determin:0,dict:0,dictionari:0,dispatch:7,django:[0,2,3,7,8,9,11],djangoproject:0,doc:0,doesnotexist:[2,7],dynam:[2,7],edit:[7,8],employe:[7,8,9,12],employee_id:[2,7],employees_num:4,employeesconfig:2,empty_permit:7,encod:0,encoder_class:0,encoder_opt:0,environ:0,envtool:12,error_class:7,errorlist:7,event:0,everi:7,exampl:[0,2,7],except:[0,2,7],execut:[2,7],expos:0,fals:[0,2,7,9],field:[2,3,7,8,9],file:[0,7],first:[2,7],fluent:0,fluentrecordformatt:0,foreignkei:[2,3,7,8],form:[9,12],form_class:7,form_valid:7,format:0,formatexcept:0,formattim:0,formview:7,forward:[2,7],forwardmanytoonedescriptor:[2,7],forwardonetoonedescriptor:[2,7],fot:9,from:[0,2,5,7],full:0,gener:[0,7],get:[0,7,9],get_context_data:7,get_next_by_cr:[2,7],get_next_by_d:7,get_next_by_modifi:[2,7],get_previous_by_cr:[2,7],get_previous_by_d:7,get_previous_by_modifi:[2,7],get_respons:0,getenv:0,getmessag:0,gunicorn_config:12,handler:0,have:7,headernocachemiddlewar:0,healthcheckawaresessionmiddlewar:0,healthz:[0,12],home:0,howto:0,html:7,http:0,id_:7,ident:0,identifi:[2,7],implement:[2,7,9],includ:0,index:6,inform:0,initi:[3,7,8],install_us:[2,12],instanc:[2,7],invok:5,is_next:[2,7],item:7,json:0,json_encod:0,jsonencod:0,keyword:5,kwarg:[0,1,2,5,7],label_suffix:7,lambda:0,level:0,line:11,list:[0,7],listview:7,load:[2,7],log:7,logging_formatt:12,logic:[2,7],login:[7,9],loginview:7,logout:7,logoutview:7,logrecord:0,lunch:12,lunchconfig:7,mai:5,main:11,manag:[2,7,12],mani:[2,7],max_length:9,media:7,memory_usag:5,memorywatch:5,menu:[7,8,9],menu_id:7,menu_list:7,menu_opt:7,menu_us:[7,8],menu_user_id:7,menucreateview:7,menuform:7,menuformtestcas:9,menuopt:[7,8],menuoptionstestcas:9,menutestcas:9,menuupdateview:7,menuviewstestcal:9,messag:[0,7,8,9,10],meta:7,method:[5,7],methodnam:9,middlewar:12,migrat:[2,7,12],model:[3,8,12],model_nam:8,modelchoicefield:7,modelform:7,modifi:[2,3,7,8],modul:[6,12],mondai:7,more:0,morn:7,most:[2,7],multipleobjectsreturn:[2,7],must:7,my_app:0,mysit:0,name:[0,2,3,7,8,9],none:[0,7,10],nora:4,obj:0,object:[0,2,5,7],objectdoesnotexist:[2,7],one:[2,7],oper:[0,3,8],operand:0,option:[7,8,9],option_id:7,order:[7,8,9],order_employe:2,order_opt:7,orderform:7,orderformtestcas:9,orderlistview:7,orders_list:7,orderstestcas:9,ordersview:7,other_app:0,out:0,overrid:[5,7],packag:12,page:6,param:[4,7,10],parent:[2,7],pars:0,pass:5,path:[0,7],pattern:[0,7],pattern_nam:7,permiss:[7,8,9],persmiss:7,pid:5,pleas:0,post:7,post_fork:5,prefix:7,preparatori:0,process_request:0,project:0,queri:[2,7],raise_on_format_error:0,read:[2,7],record:0,redi:0,redirectview:7,ref:0,relat:[2,3,7,8],related_nam:[2,7],render:7,repres:[2,5,7],request:[0,1,7],requir:9,resolv:[0,7],respect:5,restart_on_rss:5,revers:[2,7],reversemanytoonedescriptor:[2,7],rout:[0,7],routepattern:[0,7],row:[2,7],run:5,runtest:9,safeti:0,santiago:7,save:7,script:4,search:6,see:[0,7,8],select:7,self:1,send:[7,9,10],send_message_slack:10,sender:7,sendmenutasktestcas:9,sendmessageslack:9,sent:[7,8,9],sequenti:5,server:5,session:0,sessionmiddlewar:0,set:12,setup:9,setup_periodic_task:7,side:[2,7],slack:[7,9,12],slug_field:7,slug_url_kwarg:7,sourc:[0,1,2,3,4,5,7,8,9,10,11],specifi:0,standard:5,startproject:0,step:0,str:0,string:0,subclass:[2,5,7],submodul:12,subpackag:12,success:[7,9],success_url:7,taken:5,target:5,task:[11,12],templat:[7,9],template_nam:7,test:7,test_call_view_deny_anonym:9,test_call_view_load:9,test_call_view_permis:9,test_date_form:9,test_fail:9,test_form:[7,12],test_menu:9,test_menu_form:9,test_menu_form_required_d:9,test_menu_form_required_nam:9,test_message_max_length:9,test_model:[7,12],test_name_max_length:9,test_ord:9,test_send_fail:9,test_send_success:9,test_sent:9,test_success:9,test_task:[7,12],test_uuid:9,test_validate_d:9,test_view:[7,12],testcas:9,text:0,textfield:[7,8],thi:[0,2,5,7],thread:5,time:[0,2,7,9],timezon:7,todai:[7,9],topic:0,type:0,union:0,uniqu:[2,9],unique_id:[2,3,7,8],updat:7,updateview:7,url:12,urlconf:0,urlpattern:0,use_required_attribut:7,used:0,user:[2,4,7],usernam:4,uses:0,usestim:0,using:0,utc:0,util:[0,2,7,11,12],uuid:[2,7,9],uuidfield:[3,8],valid:[7,9],valu:[0,2,7],variabl:0,verbosefluentrecordformatt:0,via:[2,7],view:[0,9,12],when:[2,7],when_readi:5,which:0,who:7,worker:5,wrapper:[2,7],wsgi:12,yesterdai:9,yield:0,you:5},titles:["backend_test package","backend_test.utils package","employees package","employees.migrations package","employees.utils package","gunicorn_config module","Welcome to backend_test\u2019s documentation!","lunch package","lunch.migrations package","lunch.tests package","lunch.utils package","manage module","cornershop-backend-test"],titleterms:{"0001_initi":[3,8],"0002_auto_20210702_1647":8,"0003_menu_unique_id":8,admin:[2,7],app:[2,7],backend:12,backend_test:[0,1,6],celeri:0,conftest:0,content:[0,1,2,3,4,7,8,9,10],cornershop:12,document:6,employe:[2,3,4],envtool:0,form:7,gunicorn_config:5,healthz:1,indic:6,install_us:4,logging_formatt:0,lunch:[7,8,9,10],manag:11,middlewar:0,migrat:[3,8],model:[2,7],modul:[0,1,2,3,4,5,7,8,9,10,11],packag:[0,1,2,3,4,7,8,9,10],set:0,slack:10,submodul:[0,1,2,3,4,7,8,9,10],subpackag:[0,2,7],tabl:6,task:7,test:[2,9,12],test_form:9,test_model:9,test_task:9,test_view:9,url:[0,7],util:[1,4,10],view:[2,7],welcom:6,wsgi:0}})