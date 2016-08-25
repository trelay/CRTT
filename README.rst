CRTT
====

Only Python3 is supported.

CRTT is shortened for Common [RESTful] Test Tool; it can be used in following occasions:

* Test the reliability of RESTful server 
* Find unknown issue
* Stress test for RESTful server 
* Key String matching



Support
-------
* This tool is intended to support all kinds of RESTful server, from Redfish to...

Version
-------

0.8.1

Installation
------------
Install with pip3::

    pip3 install CRTT

Quick Start
-----------
.. code-block:: python

    from CRTT.get_nodes import GET_NODE
    get_node=GET_NODE(host, client_app_ver, port)
    get_node.scan_node()

Or use build-in sample::
    `./test.py <https://github.com/trelay/CRTT/blob/master/CRTT/test/test.py>`_

Arguments & CLI options:
------------------------

* --help: Print help message and exit
* --config-dir: Path to a config directory to pull \*.conf files from.
* --config-file: Path to a config file to use. Multiple config files can be specified, with values in later files taking precedence.
* --CLI-comp_file: The url response data comparing file
* --CLI-cycles: How many times we scan the nodes
* --CLI-time_to_stop: CLI_TIME_TO_STOP: If both this option and --CLI-cycles are set, the one which comes first will take effect.
* --CLI-retry: How many times retries after failure

Response check from URL:
------------------------

The conf file for checking response from URL is defined in file `value_check.conf <https://github.com/trelay/CRTT/blob/master/CRTT/test/value_check.conf>`_ by default, but you can also define it when run CLI, refer the help::


    [MemoryModule]	#The name of current url, can be found by key "Name"

    SizeGB= 16		#The size of memory of current url

    VoltageVolt= 1.21 < 1.30 < x < 1.40 < 1.51		#The threshold check format, it should have LowerThresholdFatal,     LowerThresholdWarning, UpperThresholdWarning, UpperThresholdCritical


If the node_name or the check_key is not defined properly, it won't check without any warning.

For Advanced user:
------------------

This application provides a config file to let user customize, modify. One can change the setting in file `CRTT.conf <https://github.com/trelay/CRTT/blob/master/CRTT/test/CRTT.conf>`_, here is the help for this document::

    [REST]

    root_node='http://10.204.29.243:8888/redfish/v1/Chassis/Defaultstring/Thermal'
    #Noen by default, This one will take effect of rest of this section.
    client_name=redfish     #The name of the RESTful client application.
    host=10.204.29.244      #The IP of this RESTful server 
    bind_port = 8888        #The port of the RESTful service.
    ver_support = 1         #The ver list of the RESTful client application.
    client_app_ver=1        #The ver of this RESTful client app
    subnode_keys= '@odata.id'	# All sub nodes should be found in a dict, and this defines the key to find sub nodes

    

    [MAIN]

    value_file=Red_lib/product/url_dict.conf    #This file is used to check the
    #response(response is in JSON format) from RESTful server .
    cycle=20                #How many cycles to scan all the nodes
    processes =4			#How many of processes in this running host

    [LOG]
    app_name='redfish_test'     #The log channel name
    logfilename='redfish.html'  #The file name to save html log file
    log_format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    root_level=10               #The root log level
    ch_level=10                 #The log level for console stream logging
    fh_level=20                 #The log level for html file stream logging
    html_color=color_2          #How we display the msg in the html file, it has options, choose one from below dict.
    color_1=err_color: red, warn_color: yellow, info_color: white, dbg_color: white
    color_2=err_color: red, warn_color: orange, info_color: white, dbg_color:blue

    Keyword_Italic=True         #The setting of keyword in html log
    Keyword_FontSize=3          #The setting of keyword in html log
    Keyword_tag_start="<hl>"    #The setting of keyword in html log
    Keyword_tag_end="</hl>"     #The setting of keyword in html log
    title=Red fish log          #The tile for html log
    console_log=True            #Display log to console?
    HtmlmaxBytes=52428800       # You can specify particular values of maxBytes and backupCount to allow the 
                            #file to rollover at predetermined size if rotating is set to True, otherwise
                            #rotate file without backCount limited.
    Html_backupCount=5
    Html_Rotating=True

    [REQUEST]
    http_time_warn=0.5          #Setting of response time from RESTful server 
    http_time_error=1.2         #Setting of response time from RESTful server 
    timeout=3                   #The max time(second) to get response from RESTful server 
    retries=4                   #How many times to retry if error occurs
    delay=1.5                   #Time delay during a next retry if error occurs
    backoff=2                   #backoff of delay
    failonerror=False           #Stop test if fail still occurs if retries.


Modules defined:
----------------

|

`[get_nodes.py] <https://github.com/trelay/CRTT/blob/master/CRTT/get_nodes.py>`_: 

This file contains classes and functions: GEN_URL, GET_NODE, URL_REQUEST and Responses check:

GEN_URL: This class is to build complete URL. 

A complete URL to interact with RESTful server is like this: :

    http://10.204.29.221:8888/redfish/v1/Managers/1

here is example to use::

    url=GEN_URL('10.204.29.221')
    gen_url=GEN_URL('10.204.29.221')
    url=gen_url.get_url('/redfish/v1/Managers/1')

GET_NODE: Scan and find all the child nodes from root(is node_path=None) or any node that is defined in function "scan_node", and put them into a list, during this scanning and searching, one can compare the value returned from RESTful server . url_list contains all the urls after scanning.

URL_REQUEST: Send Request to RESTful server, generally, the request should be one of GET, PUT, POST, DELETE. This class can handle all http errors. Example::

    url_request=URL_REQUEST('http://10.204.29.221:8888/redfish/v1/Managers/1',username,password)
    url_request.get_req(value)   #Value: a python dict

Reponse_check: It has two functions: 1. Check the response from RESTful server which defined in file [url_dict.conf] 2. Check if request time exceeds the limit.

|

`[retry.py] <https://github.com/trelay/CRTT/blob/master/CRTT/retry.py>`_:

This file is an independent module, it's a decorator and used to retry a function in a particular error occurs.
retry calling the decorated function using an exponential backoff. Example:

.. code-block:: python

   @retry(ExceptionToCheck=ValueError,  tries=3, delay=1, backoff=1,stoponerror=False, logger=None)
   def foo():
      try:
         raise ValueError
      except ValueError as ve:
         raise

**Free Software, Hell Yeah!**

.. (Contact trelwan@celestica.com if you have any questions.)


