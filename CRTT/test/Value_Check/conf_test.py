#!/usr/bin/python3
import sys,os
sys.path.append("/root/redfish/CRTT/CRTT_lib")
from get_nodes import Reponse_check

#url_dict={"Name":"FAN", "Fan_Speed":5}
#url_dict={"@Redfish.Copyright":"Copyright @ 2014-2015 Distributed Management Task Force, Inc. (DMTF). All rights reserved.","@odata.context":"","@odata.id":"/redfish/v1/Systems/123fed3029c-b23394-12/Memory/13","@odata.type":"#Memory.1.0.0.Memory","Id":"13","Name":"MemoryModule","Manufacturer":"","Socket":"13","Bank":"","Type":"DDR-3 RAM","SizeGB":16,"SpeedMHz":2400,"VoltageVolt":1.20,"DataWidthBits":0,"TotalWidthBits":0,"FormFactor":"DIMM","SerialNumber":"","AssetTag":"","PartNumber":"","Rank":"","ConfiguredSpeedMHz":0,"MinimumVoltageVolt":0,"MaximumVoltageVolt":0,"Status":{"State":"Enabled","Health":"OK"},"Location":{"Pod":1,"Rack":1,"Drawer":1,"Module":0,"Blade":123},"Oem":{},"Links":{"ContainedBy":{"@odata.id":"/redfish/v1/Systems/123fed3029c-b23394-12"},"Oem":{}}}
url_dict={"MemberId":3,"FanName":"FAN2_TACH","Status":{"State":"Enabled","Health":"OK"},"ReadingRPM":6600,"LowerThresholdFatal":0,"MinReadingRange":0,"MaxReadingRange":25500,"PhysicalContext":"domain(29.2)","RelatedItem":[{"@odata.id":"/redfish/v1/Systems/Defaultstring/fan_cooling/2"}]}
Req_check=Reponse_check()
Req_check.confcompare(url_dict,"/root/redfish/CRTT/Value_Check/url_dict.conf")
