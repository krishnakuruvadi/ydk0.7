from ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_cfg.interface_configurations import interface_configurations
from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

class CodecTest(object):
    def test_encode_decode(self):
        intf = interface_configurations.InterfaceConfigurations()
        iss = intf.InterfaceConfiguration()
        iss.active='act'
        iss.interface_name='Loopback0'
        iss.vrf = 'red'
        intf.interface_configuration.append(iss)
        codec=CodecService()
        codec_p=CodecServiceProvider(type='json')
        json = codec.encode(codec_p, intf)
        print(json)
        obj = codec.decode(codec_p, json)
        print(obj)

