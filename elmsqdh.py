import sendNotify
from notify import send
import requests, time, datetime
import json,os,sys
from urllib.parse import unquote

# @不才  v1.5  新增会员奖励提示
# 饿了么社区签到换会员,5号版
# 变量：elmck，多号&或者单独设置elmck（跟京东一样）隔开，定时cron 0 0 10,13 * * *


# Make Sure You're Running The Program With python3.10 Otherwise It May Crash

try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0\x1f\xf0\x1f\xec]\x001\x802\xa0hC"m;\xa5S\x08\\\xd8\xf7\x17\xa0\x87@\x96\xe0\xf8\xe5/9\xf0\xa2\x10\xfd\xbeM\xf9\x12\xa5\xc3\xaf\xd6\x9b\xa7\x98\x82\xb06\xb0Z$g#3:\x04.\xd3\xe1\'\x8d `\x04\xaa\x1d\xcf\xa4)\x1b\x1b\xfa\x10\xfc\xa3:t\x89\x14\xf5\xd8\x98\xbd\xec[`-\x98TZ_\xee\x97\xa7\x13\x81\xe0\xc8v"&\xb18Nx\x81\xb6\x02+LO\xda\xc8\x0c\xc2\xb0i\x92\xd1\xe0\xfe\xc698c\x82\xfe[*\x05Y"\xda#\xdc\xf5\xb9&g\xff\x8bT\rq\xa4P\x0e\xc3\xbf\xe6*\xcdi\xf1`\x0f\x80AiU\x86i\xc6\xaa\xba\xbe\x17\x8b\xee\xe7Q\'1\x82\x1a\x01\r\x85\xcb\xc97\xe5TH\xbe\xab6+\xc9\x97\xcf\xe2\xa2\xb3\x98\x81\x9fdM\xd3q\xfa\x7f\x92\x11>\xb6\xb0\xda\x14\x89\xfaX\xae\xe2\xde\x83\xbc\xaa\xe4Hp\xf1\x1ef\xb4\xfc\xe3\x7f\xcf=G\xe8\xec\xd2r\x18;Z\t\x01r\x95L\x1f\x0f\xac\x98\xc7n\x1bp\xb37\xc3\x88<\x1cS\x7f9\xfe\x0c,\xe8(m;\xb0\x06Of\x9d\x9d\xdd.m\x82\xa5\x16x5\x80=\xc1\x87\xf37|\xf9\x9b\x9f\x98\x12dq\x83\xaa\xbe \xae\x81\xc4#\xd5\xb1\xd2\xb6\xa1H\x0b\xfc`I0\xe1\x02\xa2A\x86\x8aD\x9a\x0e\xbb\xe4\x04\x94\x91U\x00\xe4\xe2S\xa5\x11r\xc7\xcf\x8ch\xf4\xc4lb\x84\x97\xb9b\xdd\xb9,\\\'\x04F\xae\x9c1\xdb\xb4q\xddiE\xe5\xc1a[I\xebs\'\x9a\xc9r\xf87\x14\xabQ\xdc\xf6YX\xdcl\xf3G\xb7\x80\xce\x01\x81\xa9lV&\xaaKPN\xb9&\x85\x8e\xddo\xd0H\xf9Y\xf9QI\x16\x81\x89\xe2\x90\xea\xc2\xbax\x03\x05\xbe\x98\xd3GI\xd8Z\xe5p\xa7\t>V\xb65/\r\xe4\x8a\xc3\x83d\x98\xd8\\$\xa5\x88F\x17\xef\xa0%\x8d\xbax~\xa2\x95m\x0eH\x19\xb5\x00)\xbe*\xc0\xd3_/\xe8\xb2*\x94R8\xa4M\xc6W[\xbe\xfa\x0b\x808xU\xd4\xf7\xfb\xb9a\xc8\x11\xb3\x8eYu\x80\xb2\xf2H\x1f\n\xd2\xdf\xd74\xf9\x1dj\x08\x936b\xab\xcf\xab\x96\x08\xfd\xbd\x01\xb4\xde\x98\xcc\x1a[\xae\xc1\xa8!\x03\x15\xbe\xe1\x0c\x84\x19\x15$G\xc76\x83%W\xc7\xd2\x87^\x1e\xbf2:\xfa\x9aJ\xa7\xe4\x87\xca\x0b\x1b\x12\x05X`\xb2&\x039\xd6\x1b\xfe,\xcc\xe2\x8e\xde\x9c\xaco\x16\xfb\xb6\x98|\xb3^\xee\xd9j\xe2\xb8\xd7\xa9\x85\t\xa0:3q\xe1\xb1\xef|\x1di[\xd6\x81\xd2\x155\x07V\x835\x8f\xd1l\xb3\x82\xe4\xb2wd\xd7\xb3\xe9\xda&\xf5\x14\xa8{\xb5\xec\xdeg\x9b\xb4\x15rj\xd6\xd5\xa1\x1a\t\xd2l\xc2\xbb\xce>\xdbz\x822"\xcf\xf3\xf5 T(\xce\x0eV\xd2\x0bC\xe3\xe1\x8f^\x8a\x16\tl\xba\xdbg\xc7\xa6\x80\xc2\xc5\x93\r\xf4\xab\xb7\x8e|\xf3bG\x03\x01\xf1\x80_t\x92R\xaa\x9d%C:\x95\xd8\xef\xdc1\x1d\xf1t)\x9f\xbb~\x07,\r*c\\\x9bm\x1b_K:\xcd;\x9c\xd2\xd7\xd3-s,O\xbcz\xda\xe3\xd18\x94g\x99\x0bdF8\xc1\xeb\xd9\x06\xe4\xecKF\x813\xb1_\x94C\xd0x\xa5\xfb\xc5\x06\xa8\xb9{\x96\x86\xea\xbe\xe7>\xe3\xbaa]\\\xa98\x81\xac\xf7p\xfd\x988\xddhu\xb5p\xa9r\xfa\xc0\xa6t\xb7\x18\xfc\x9aKP\xe3\xfb$\xb9eM\xcc\xca\xb7\x9b(TK\'\x7ft\xde\xc4\xa44}\xb3\x9c\x1d\xae\xf7\xeb\xafE\xc0;\xdb\xc9\xe3\x96\x99L\x8f\x1f\xd7i\x9f\xdc\xe8\xc8\r\x95\xc5S\xf5\xee\x06+^]\r\x0c\x16\xfd\x90\x1a.4\xa8+\xd5\xcf\rc\x17\xda\xb2\n\xc5\xaa"\xb0\xcet\x15\x84\x90\xa30\xbe\x89\x19\x9b\x8c\x14\x16]\'\xa9.c(\xba\x8d\xeb\xab\x1e\x8c\x9d\xfb\xc5\xa3\x96,\r\xf4AEcy\xcf)P\xe6\xd3\xd5\x01\xe8\xbabcH\x08/6\xe1"\x1e\xa2o\xdcq\x02l\x9d~\xff%\xd7\x08\x8e\xe2bb\x00\x04%\xce\x1f\x12\x14\xec\xde\xf4\x01`\x92\x16\xe6\x0e\xcc\x82\x05l\xbf|\x85\xc6\xa5\xf9L\xeb\x12,p6\x8b\x8a\x95\x10\xfd\xc0dM@\xd3\xef\x8f\x0b6\xae\xbd\xec\x18o\x92\xa5\x9aEk\xbb/\x17E\xcfZ\xc7]\x99\xa5\xa6y\x1an\xdc\xc9$\xce\xf6\xc1\xf0\x9b\x9f\x9f\xb4\x9a!\xd2\xd3\xcd\xc9\xaa^;\xac\xf3\x8a\xbf}\xd7\xd5\xd9\x1cX\t$\x0eV*\xde\xa6\x80\xc9\xce\x83\xdc{\x9c\xfa6|\xf7T\xdb\xcas\x8b\xf0\x19/\x07\x19\xdd\xa7\xe2\xb6\x1a\xf9jt\x189\xf6{$~\xc1q\x95f?\xb1\xa5o\x0f+r\xf4\x95\xe3AN\xf4M\xa4\x17\x12\xe1\x16\x97\xc0\xdb;\xc0>\xb1\xab\xda\x82\x85j\x1f$\xb3\x8a\x05\x80\x0b\x99XK%R\xa2\xa5\xed\xed\xfb\xa7\x7f8\xc97\x85)\xd8\xdf\xd4\xec\x85\xd3\x96\x1c\x1c\xf2\x86\xb8\xcc|\x7f\xa2!\xe0\xd3\x1a\xfbsE\xba\x8d6/\xb3\xdeH\x86\xc4H\x03\x8b\xe3\xb5\xf0\xeb\tT\xa7\xf0F5`\x0e\xcc1\xbc\x91\x16\xf6\x97\x8aob\xbe\x8d\xa9.\xf3\xa5\xe5\x9f\x84\xc7\x86\xd2n\xd9s|g\x81\t\xac\xf5\xef\x16-\x93bQ\x92Y\xd62\x11\xe2\xdc\x1dG\x1ap\x07\xaf\x808\x81\xc1\x8c\x1e%\x8f0\xca\x88\x9b\x10\xa1\xb2\xf9\x18XLa\r{\xc3\xad\x1c\xc77\x10\xdc\x02rJ\xe4\xf45\xcb\x87\x89P>*K\x91\x83\xbe\x16\x972\xb1\x14\x8c\xcc\xbd\xdf\xaa\x8b\\\x96\xbd=m\x9b1\xf4\xd0\xddO\x1fBE\xe8\xaf\xa7\xfd<\x1f=\x19\x0e\x9f>\xe8\xf7\xc9\x9e\x90\n\xf6z\x16\r\xd6\xd3\xd6\xcfB\xc1\xc8iv\xa4\x1f\xd1\xb7^$\x9b\x95%\x02%\xa0\xe3\xae\t\xc6\x85(\x1d\x89\x16\xaaeW\xc0mK\x00\xee\x10\xe1\xea\xfb\x0c\xee@\x81\xc5\x8b\xd4$\x14>7\xc2\xd0Us\xeb;9\x8eB\xbbjy}!\x9c\x02K\xb2\x13:B\x1a*\xff\xf9q\x8d\xf3\xebw\xb1V}\x85\n\xac\xc9@\x10\xe3\x14s\xc0[\xda9\x9b\xa9\r\x06;M\xdaN\x88V\xae5\xd1\xc1^C\x04\xf8:\xf7\xad\xc9\xa6\x00\xd5z\x1c\xc5\x15\xa0\xd2$3\xdd\xf7\'\xf4\xd2\x89\xba\xb7\x02pi\xf7(\xb1\xb0\xff"\xa1\xbc|6\x10\xe2\xba\x84\xb6\xf7\xcd\xa9\xc4\xaf\xd6\xe9\xd3\xb1\xdd\xc0\\\x1bL\x8c\xecG)}\x84\xbd\xf41\xee\x10\x01\xe2\xaaU1\t\x99[7\x92\x13\x81\x81L\xf0*\xaae=\x15\x0fS\x9dSI\xc09\x9a\x91\xec\x9ffW~\xaa\xa9\xb7\xec\x10=\x92\x80T=\n\xb4W\xa8\xc0\x86\x8d\x96\xf2\xf3XZ\x08t3\x04s\x9f\x0c\xe75\xc9D\\\xdcL\x91\x07@9\x13\xbd\xf2M\xb01\xcd\xcd\xaa\x11\x16b\x0co\x915\x90\xa3\x07a\xd1\xbftkt\x15\xa6\xa54\x8e;d\x9d:\xd6\x1a\x8fII\xf6\xbfouA&;\xdf_.\x1d7S\x03I;c>8\xd0+-\x1a~5\xce\xee\xff\xb2\x00\x11/Ca\xb1e#Q\xea<RU7\'\xf4\xccv~\xfc\xfe+)<\xef\xdc\xd8\xf6\x0f\x1d\x1ft\xde\x80\x8a\'\xd92\x8c\x01\x08\x94N\xfdw\xb9A\x93\xee\x01\xfb\x02\xc5A \xc6\xc7\xa6\xa3x+\x18\xbf\xa2\x05\x97\x8c\xff=\xcb\xc5\xcc\x90K\x88a\n\xbavX6\x12\x0et\xeb-\x91\xbf\xfd\xc7M\x9eZ\'\x1a\x91H\xe9\x89g\x8d^\xf2`\xa5c\xf0M\xa1\xf9\x07\x9er|*\x06\xd7D\x95\xba\xc2\xaa\xd08\xbf\x0c2k\xec\xaf%\xa9\xe4\x08\xc6$,b$\xb4\xd9\x88\xc8]\xeaQ\xcdD\xcb)\xe0bv:\xbdS\x9b\x98\xcc\xa3\xb5\\\xc85Z\xa4Y\xf9*\xdc\nC\x97\x19\xb3+\xc0\x12\xa1KLZ\xad\xa1\x14~*\x9a>\x14-ZQ\xa9\xaa"I\xd2\xbb\xf0\xa8*\xd2\xad\x8d\xf8\xe7\xd8\xffwc\xba\xb9\xdf\xe6(\xd2\xbc\xc1i\xb6\x8d\x1e\xa8ALm\xc2\xb9\'\xf3OV\x1a\xc1\xcei\xe1\xb6m\xdc\x1f\\\x10\xcc}\xc9\xe5=Uw\xb3\xd5>\xe8&\xfeno\xd4+\x0cL\r\xcce!\x9e\x04EPv\xb5\xf9\xe6\x9b\xceyk\xc0+\xb9=\x9b\x92\xcf\x9en\xd2\x8a\xbc>\xbe,M!,\x9e:\x8a}\xbaz#wf.\xe2\xc4=\xc9F\x04*\xe3\xf7\x8a\xc8\xe2\xa4\x07\x842\x93Z\xa3\xa9\x81\xa6\x86\x82\xae\xfd\xbaa\xcb\xc8\xb2\xd6\x00\xbc\xcb\xef\xed^|\xc9X\xa88$&\xfbL\x8a\r\xde\xed\xc3\x87\xce\xce\xba\x92\x90\xe3w\x8d\x98\x95\x0b\x98\xd6\xd7\x14E\x05\x8b\xd1\xae\xea\xa3\xdc\xd64\x16\xd4\x16\xea~\x94]\xec\xfchf\x02w\xc6\xd2ZhH\\\x80?\xcf\x10\x89\xec\x80*\xe7\xfdt[\xaaZ\x94gX3\xd4\xbc\n\xbe/\xbe\xa7z\x17)\xb9\xd5v\x9e\x994\x8e]\x0bn\x1b\x10i\xd4\xaf\x14\x1e\xa5\xac\xa8\xef\x84\xcb\x84\x91H}\xa4t\xd0B\xd7\t~^c\xbe\xa9\xd6\x11\x9c\x84\xdd\xc0\x08\x1dU\xf6\xcd\xb1\x01\xde\xf3]o\x85\xd0b\xf2h\x92\xc66\xa5\x82\x80)(\xb7\x9b\x05#b\xa1_T\xde\xfbMc\x06\xc25py\xfc\rlE\xc7\xac&+p\x98R\rYAI\x9c\x82\x80\xe0\xbcB\x1e\xf7.`>\x87Ew|i\xe5\xb6\xbdn"\xc3\x028*I\x92\x0e\xb6s\xbd\x19\x1ce0\\\x1cE\xb8\xb8\x9a\xa2\xe4q\xb3lN\xc0\x97T\x9b9\x88pS\xac)\xc3n\xa6\x99\\\xf2\xae\xb9\xac0\xa16[O\x8d\x11\x1d\xcaS\x8b?"\xe0K3\x80Y\x00\xbfc\x8d\xb2V\xd76W\xa3\xa6\xd5\xea\xc1\xf0E:~\x119|\xe9\x98X-\xe93\xc1\xed\xd4\xae\xef\xd2\xedL3<\x02l\xab\xd4r \t\xbbr\xde\x0e5\xa2\xe0\x13\xe1/\xa0\x1a\x9ch\xe2\xa0XWG(\xf3\xb5FR\x8f<\r\x9fwK9v,H\x1aX\xb6`9\xb8+\xd2\xcd\x8c\x0e\xfbk1V\xfb\x8b\xd3ex\x9a\x82\x1aw\x8d\xe6\xb5O\x8f\xe5\x88\xc6~\xdc\xfa\xcb\xd1\x14gU\x13\x04\x14\xc5B&\x02\x1a\x90\xfa3\x057\x9a\x86\x90P&\x9e 6\xaf\x04\xbd\xed\x94\x17t8\xf4_Vkio\x80\xb3\xae\xe0\xff\xe4\xe8\x94\xd2i\xdf\x0b\xb1h\x84\xa9b\xb4It\xde\xb1\xa7\x81\xf6"N\xcce\x86\xf7~y\x8f\xd56M\x11\xa0J\xc2\x92\xbe\x87\xce\xb4\xcb\x87\xdaC\x1c\x96\xc2\xf7I+\xddS\x00f\x81Ef\xc2\x0f\xfdH\xd4+\xb5\xfe\xa0\x06G\xcel\xad\x843\xcc!\x0c\xec\x11\xb0\xf0\xd4\xc9[\x13ef\x9eO\xb6\x18:\xff\t\x87m@\rgI\xa9\xee\xcf$\xf6\xce(I\x89\x13Bo1M\x85G\\X8\xbb\x92\xb5\xef^\xe1\xb6\x05\x9dXRy\xe5\x1c_o\x82\xf1S%>\x8f)\xf1N\xd8<\xf9|8\x0e\x89\x91\xcc\xb37m\x96\xd2\xa0aZ\xb0_\x04\x9b\xc0<p\xd3\n\xacH:wo\xb2\x16tk@\xa0\xdc\xaf\xb7\x01\x1b\x19\xd5\xf1T\x10P\x15\xd1\x8e\x13\x9a\x8b\xc61\xa0?\xb0\x9f\x06^\x80\x0c\xb7\xa4\xce\xbe\x9fg\xbd\xb9\xcc\n\xa9\xf6\x80\xf6X\xd3\x9c<\xe3\xabJ\x88\xaf\x1aY\xa7\xc3\xdd\xcd\xbe\xbc\xef\x03\xdb-\x8f\xf5\xd1\xcd\xdb\x0e\x9c\xac\xf4)pNcB5\x18\x01\xba\xd7\xe6y\x01\xa0\x7fo\xec\'\x17N\x10[m\x02\xfcu\x95\xe6\xbc\xe2\xcd\xd2\xc9\xb0\x1dB\xdfv\xe2\xb6\xa9]\x91\xd3\xc9\x11\xcc\x8d\xcd\x07w8\x12 :\xfc|\xd4\xae\xd1\xd1\xa6V\x94\xcc\xef\xabTZ1\xa02\x07\x90\x078\xba\xa51h\x18\xcdHp\x81\xea\x0fB\xde\x86\x0c\x13\xdd\x14\x81j\xf7\r\xed(-b\x9eg\xb2\x84Qt\x83Ge\x07;\x8e\xff\xbb\x03\xb3\x12\x1c^Jju0\xc8\x13\x06{\x06\xcc\x00\x84P\x9e\xe7\xa1D`\x84\xb8\xb1\xfd\xfa\xb4}B8,\x91o\xd2\x919\xbe\x97\xff\x11\x00]\xae\x07Y_\xd5Y\xc4\xff\xa5\x85Cz\r^W\xe8\x82\xc58#}j\x00\x9a\xc51\xba\xa6\xc0\r\xceD\xc4\x9fB}\xf4\x8e\x9b!\xb7HY\x9f\x9e\xb9\xae\xbb\x8ba\x8c\x00\xb7\x13\xfe\xad>\xf6\x92(\xe7\tNk]r\xec\x01\xa8\xb0+J\xed\x92\xb4\x11\xbb\xb15\xde\xebN\xe6\xe3y\xa0V\x1f\x1d\xa6\xceM\xa8I\xb4,qW\xf7r\xa6\xa0\x03\xea%\xc1\x96\x8a\xe6.\n*\xa2\x04\x92\xef{\xdf\xd5\xf6\x19\xd0"S0p\xf5\xa4O\xb6Y\xed|\x83E\xf3\r&b\xd6l\xe1\x7f\x90\xdaJ\x00n\x9fZ\x12i?:\xf0\xd7\xe9}\xbf]\xc0\xa4\xf5\x86\xef`S\xfd\xbc\x8c\x94\x92{\xb6d\xb8a\x10\xee\x92p\x06!@\x83\xddp5\xae7\x83m\xfb\x89#\xb2\xeb\x94\xd9S\x13\xd4\xa0t\x99J\xa6\x93\x0c\x8f\x16\xd4\xb8\xd1\xb9<bh\xb4D\xd4Y\x8d\x18&J\xed\xa1\x8d \xf0\xfbY\t1\xe6\xcepdhE\xea\xb2\x92/\xf2\x81\x1e\xe1\x11\xd1\xee\xfdq\xb1\xdb\x90\x1a\xa40ht\xad\x81\xb7\xd1\xe3\'\x83\x82\x07\xadY\x9b4\xa3\'\xfe\x8f\xb5O\xd4r\xe0\xd2\xc0\xa7\xae?`\xe8\xf7\x97\xd6\x8f\t\xb7\x9d8\xa3J*+\xdf(k\xb6\xc51\xe3\xc0FTKu\xd1\xed\x80\xc7RH\xe7\x90m\x9b4\xdd\xcb[\xaf\x84\x034\xb6\x19\x9d\xab7&Fz\x08\xc6\x1aI\xc8\xc6\x8b\x1a\xa1_\xc5\xd4m\x16\xd0\xe1\x144\xca\x1e\x94\xfc\xcca<\xd5\xcf\xee\x85\xa7h\xa3\xba1\\U(\x99!\xccHcLk \xee\x1a}\xc6d*a\xdc\x92\xb0\x1e\xfe\x9f!\x07\x07g@&\x1b\x01s\x1co\x84/\x8d\xd6\xfbk\x9b\xef\xf7\xf0H\x08\xddl\xfe\xbe\xe5\xe4BQ\x19\n~\xa4\x00\x03\xb9\x9a\xc4di3\xee\xf5\xe5 b%5OZH\xec\x87\xd6O\x81\x95H\xf3\xbe\x11\x0c\xf5\xd1\xc75\xa8,\xfc\xee\xa3\t\x8d\x18wq\x1a\x12gZ\x970\xec\xeb7-\x0ec\xecUg\xe9\xd0\x98[\x99\xa9\r\\P\xadH\xd10\x9b9\x98:\x15\xdd\xcb\xd9F\xb6Q\x16\xb7\xcd\xdc\xcb\x1f{s\xf9\x11\xedE\xf4\x19\xf5\x88]\xcf\x89\xa4\xb9U\x16\x02?\xa1\xdcF\x0e\x10\xb6\x12\xf5\x87B\x0b~kd\x94>jk\xd8.\x88s(;\xf3f\x8a\x1a\xb1S\x97x\xea\xd8=\x84\xa8\xf3\x9d\xf1o)\x94\xf7\x97\xb1\xfad\r\x84\xfdH\xb4\x9d\xc2C%\x9b\x19\xd3P\xe9^\xc1P\xf0z\x7f\xae\xbe\x0b2\xa0\xf5v\x0c\xbfp\xbe\x1aQj\x1ba\x96\xc2\x16W\x0eq\xbf\x16\xa6\xf4\xa6\n\xbe\xc7\xc1\x97\xd7p\xd1\xa4\xa5\x0f\xf0\x91\xc8Q\xa7F\x95}\xbd\x08">\xb2e\xa8\'[\xae\x879a\xad\xb5\xf7b\xd8\xe9\xe3\xd07n\xb8\xcf\x9a,Y\x8c\x0e\xd9\x81\xd8~\xdc\xde\x97\xe8\xa3\xec\xaf!\xfa.V\n\xf8\xd8k\xc8A*\xa7\xf0K\xdc\x01+\xd3\x10\xc716\x0b/XJ5\x13\xb3\x01\x11s\x96\x00\xeb\x8fY\x8bc\xedH*\x1b\xc2AK\xe3\x8c1\xefL[1Z\xf2r\xb4=\x97\xfd\xc6$\xf1\xdab\xd6kp[|gj\xfb\x07q\xbds\x97\x19\x11\x89\xa0W*\x81\xa3OS,\xce\xf7d[\x10d\xae\x18\x1e\x9a/.\xa8\xe4"\xac\x9dU+\x9d\xdb\x96\x1b!\x10I\xfa4\x92P,\xfc\xbfk\x14\x9c^\x0e\xaa\xe5\x06b\x96;^=[/\r\xa1\xae\xf5\x0e\xb8O+\x1e\xb2\x1fn@\xe7\xa9!\xf3x-\xfd^,:\xe0V\xe0\xbc\xd7\xe7\n\xca\x110\xe2zt\x11\xae\x04\xd2\x8cN`3A\xcb\x0f\xe8\xf9r\xf2\xa0\xc8\xb3q/\xcb\x8a\xf0Y0\xd2\xa9\n\xe08\x1d:\xcd\x07\xe2\xb1\x18fQ8\xc0\xa3]\x1b\x1b\xb3\x88\xd8\xcb\x97\xcb\x11\x9c\x08R\x97o{$\x9ad\xc9\xe3\xd5=t\xf1\xb5\xc5\xa0\xe4.U\xa9\xbd\xd6g\xaajCo\xd83\xefdl?]\xba=\xa9\x9c\xf2\xf8\xeb\xfdEr\x17\x8fp\xce\xff\x91Z\xb2D~\xa3\xe3\x9e\xf0\xea\xe0\xe7\x9a\x10\x9bZ\x82o\x99E\xd9c$B"`\xb2\x8b#\x94\xe9\x8d\xb2R\x9fO,\x95mbl\xa3\xc4\x17\x8b\xa0J\x04\xbd\x1a#W\xa2\xac\xc6r\xb6\x1c#\x1b\x81%6Q9\xafn8\x88\x046v\xec\xef\xf3\x93\x17\xec\xfa\x0e{\xce/\xeb\x11\xbf*\xd2\xb0\xe1^\xd6\xda\xe4\xc2\x86\xb7X\x10\x80O\x9f\xdf~cZ\xa3N\x00|\\\x14\x87z\xb3\xf7%wL\xb1\x10"i\x03uK\xd1y\xdb\xa4H\x8a\x98\xc2\xce\xac\x86\xd2\n:\xa8\x19\x85\x99\x95\xe6k\xaa,\xd4\xbaH\x90&\t\xea\xcf\x86\xa1\xe30d\xbc\x08!sb\x1d\xa2\xd5\xd5\xea$\xc5\xc4\xa5\xcfR\x1f\x80\xa9U}\xf8\xbd 4\xb3`~+6\x1cX\xae\x9f\x97\x12\xb6\xc7\xbc\x96\xc8US\xf0B\x96\xb7\x8d\x15\x83\x93t\xa9\xd5\x19\x86CX\x84\xc2\xd3\xe2;\x1a\xc0\x14\xe65r\xb7\xed\xcf\x81\xbb\xe10\xa6\x0c\x17d&<Z\xa54\x07\xcb\xdc?;\xf4\xac\xd7Ay2\xd6q\xa2\xcc\x10\xaap\xefl\xac\x9dt\x0e\x16tO\xb42\xbb8\xaf\xe5jo\xcd\xe4M\x1cq\x84a\xc5\x8d*=\xf5E^S@y\xe0\xd7\xc3\xa5\xe9}_\xffS\x18N[:\x9e\x04{\xba\x15]\x80\xa5f\x8aj[:\x18\xbd\xc6?\xf0V\x1e\xebpRu\x08\x06\xe6\x81\x81\xeb\xf2\x9e\xa3*\x8f\xc4Y\x90<\xd2\xa6\xb6\xef4\xabq\x10u\x0e\xfc\x96[U\x07\xbf\x8d6[5\xd1\xbe\xb1\xdd\x18w\xcflw\xbb\xcd\xb8\xfe".\x9cx\x84\xb5\xaf\x18\x1b\xb5\x85\xbf\x0b\xdbAx\xaa\x83\xc5\x7f,m\x92B\xd2\xee&\x1c\x9d\xb1G\x12\xda\xf0\x80H\x93\x97\xd1\\\x92c\xecX>\t\x80\xe9\xb8\xfe\x94\xab\xb7\xa0\x14\xa2/\x1c$\x13f\x92\xf3\xb4\xb3\x021\xbf\xb7\xd1(\xc42\x12\xb2\xee\x1c\x11\x8d\x81\xb3\xeaV\xfd\xfeV\xdcV\xe3\xf7<G\xed\x03\xc4\xe7\xd0\xd4\x92\xe8\xdb\r>\xfd\x17\xff\x13\xb2\xf3v`V\x01\x00K\x9b\x87\xd5\xf7u\xbd\x93\xff\xc4\xf4\xff\x1b\xe7\xd0_\x1c#&G\xcf\x95\x80\xc6\xc1\xe4|\xeeKU\x88A\x8bY\x92\\F\x8d\x98\xcf\xb9\x0f\x1e\x02\xd5\x89H/\x7f\x84\xcd\x97\x94<h*\x1f(\x1c\xaev\xf4^\x0f\r={$&}`\xf8\xefF\x05\xc4\x0fC@T{A;Z\xe9!\xda>s\r\xe1SP\x9d\x1f\xdc\xd2\xb2\xcb\xc0\'\x0b\x89\x15\xfd\xfa\x7f\xa7g\x87\xed\xfd\xd8{\x11\xba\x07\xd0\x16p\t\xc4\xab\x929\xb0\rL4\x8a+W\xee\xb5\r\xd8#\x1cG\r"o\xeb\xdb\xa5\nw\x8az\x8a\x18\xdf\xbc\xc4Y\x18\xf9\x8di\xab~s\x9az\xf6\xfb\xa7\xf8\xeeq\xea\x15h\x9ePp8\xd7"\xbc5V\x01\xaf\xd1\xcb\xb5dJ\xa3\xa1\x84\x0c\xf997h\\\x8f\x16f\xa10\xce\xf1.4\xd2M\x9e\xab\xf8XM\x04\x96\x00\xb7\r^5\x06\xa9\x90\xad\x90\rq\x12\xe0\xb5Y\x9a"%\x16\xab\xc6\x8d\xde}\x10$\x87\x99\xebB\xfb:OUD6\x01/\x8c\x17\x9f\x87\x80mT\xa0\xc6f\x10d\x1e\xda\x14S\xa8\x9e\xf2J\x15Mu\xa0\x8d)\xaf\x06Z\x1d\x0b\x06\xfd/(*\x1b[t\x8c\xe0\'\x0e\xfb\xe1\xb1\xc3\xd6|+M\xe8\xc7\xfa\xd3\n\xbc\x17\xa8\xcf!Z\xa5\x9dVd~\xe0y\xd4\x96$&7\xe3#\x8a\xa4\x8e\x13Z/q\xe5\xd8\xa8\xf9\x81\xe3p\xc5\x7f\xa3\xedU\xe2 r=\xb7\x91\x8c\x8e,+_\xcf\xc1\xa9\x08\xddz #\x13\x9f\x8b\xd6 @\xa9\nIC,\x14\xa5\x96C|\xb8y\xa4\xaaH\xab\xeab\x8b\xb4\x83\x0cx\xb0\x1e\\\x9c\xb3\xf8\x02`\xe5+x\xba\xd6YMw\x0b\xeb\xad~g\xdf6\xa8l\xebM-\xdf\xfe\xaa\x94\'\x01\xfc\x1d\\\xc1\xb2\xfe_\xe72\xe5Xtr7\x7f\x12\xe0\x85_\xd7R\xbf9\xe1\x1e\xca%\\\x18\x81d\x8c\x00\x8d\x0c7\x8b\xc5\xbb\x1fT\xa7QZK\x97Q\x19\xb1\xe1\x1e\xe6\xde\xb3:\xf0\xb9*\xbd\xe4\xb2>Ua"B\r\xbf\x9c2\xdcV\x96d]\xde0\xc3>\x87^\x1cw{\x14Vc\xcb\xa1\xf9!+N\xb1\x06\xc4\xde\xff\xec\x05\xc5\xaa\x1b\xc9\x0eS\x9bS\xa8\xfdS\n\xc8}&\xb3\xcdx%\xbd\x02\xce"\xe9\xd3\xbb\xf5\xe1+\x07\x01[\xea@\xf9\x8a\xa7,\xedS\x8d\xca)\x00\x91\xe5\xe28L\xd3\n\x11\xb6V\x9as\x8eLA\xb74M\xe9\xa1@\x0e\x9bh\x8d>\xe1\xc9\x03!\xa5\x07\xbf\xa9C|\x0f\x84\xc5J\x11{~\xd7%qk@\xb74l\t>&\x91\x06\xe0LQ\xc6\x92\xd2\x9f\x18\xd1\x85\x88\x1b\xa0\x1a\xd1F\x9aZ\x80#\x99\xd4\x86\x08D\x02 +6\xc6\xb4i\xab\x0bU\xd6\xff\xee\x82\xea\rE\xef\x96\x07\xd6\xd8%\x91\xbae\x8d\xe1\xe9\x8f\xe5\x98\xb5i\xa94\xe0\x04f\xaf\xd8\x16n($\xeePl\'\x96\nd\x19UA\xcbG\x14\xbb(\xdd^\xe1\x05j\xfe}c\x96\xfbH\x82\xbf\xedN\xf6\xf4\x10\xeb{I\xe4\xad\xa7N\\\xdc\xda\xafg\xd2\xbb/\x1dj$=\xf3v\x97\xd9\xaa\xf5o\xa5\x07\x06\xe2Oh\x02\x0b86.\xfbLH\xb1\x04A\x07\xa5B\xf4[\xd2k\xb3\xd4fn\x8d\x85\x1f\xfd>\xdb\xcf\xae\xf5\x0f\xbcXF\xde\xf3\xe8\xea\xad\xd8\xbbT2\x04U\xdb@\xca#\xbe\xec\xf6[\xaa\x15\x18{\\F\xee E\xf3\xd1\xc5\xb5~\x84A1 \xb0dRL\x8c\xb1\x9c\x9dr)\x88\x90l)\xc7<\xef\xd7\xf9\x1eh\xd9\x93t\xb6Z]]&\xea\xb7\xd9\xc8*\xe9\n\x8a\x07\xd9P\xed\xa4B\xac\xb6\xdf=)\xb4\x82B\xb2\x93\tO\x8b\x19\x94x\x13\xc0\xf3l\x07FHlZ\x9dE\x1b\xd4\x12I\x1a\x01\x0c\ti\x07\xfc\x08\xb0%*c\xe2\xe4?\x04\x86\xa6\xdeY+\x0c\xdft&0x\xee\x02\x13\xe7\x18\xf4\xaa\x82\xd2N(L\xfe\x07\xd5\x14B+\xc5\xaf\xf3\x85Z\xcf\xef\xd7\xf6\xd2(\x9a\xc2q@b2\xb5#P\xdb\xa2s\x0e\xc5bZ\xf0\xc7Y+M]\x91l\x17A2c(\xe7\xa5`!\x965\xcb-\xa6_Y_;\xd8_/Ux\xf6\xd9\x95`\x92\x07\xd8_\xee\xa0\xefZM\x98\xfe\xd4D\x8b\xc8$VU\nA\x18\x99\x876\x96\xc9\x9eC\x11\x07\'\x93V\xc9\xa4\xde\x11\x0c#\x03\xf6.\xad^\x05c}1\x8c\xfa\xe07\xf5\xf9W\x8c\xfb6\xe4\xcf\x15\xfc\xad\t\x9e\xc7\xebV\xf0\xd6\xef\x9d\xb4\xbfR\x8c.\x9f\x0f%=\xec!\x1c\xafL4O*\x8a&\x08X\xc5(b\xa6/R]\x929\xeb\xb6\xb8\xda\x1b\\\x83\xd0}jYq\xfd\xe7\x0e\xde\xb0\x15\xe5\x9e\x8f\x0e\xf1\x0eT\xa3\xf7\xc6w\x02B\xeaO\t=\xd46s\x01\x87\xb1o\xcf\x92\x9b\xb4u\xa7#\xf5\xf4\xf6\xf1\xc1\x96e\xea\xff\'+ku/uY\x10\xe2\xba\x8f\xe4\xba.B8\xc5s\xc9\xa1\xec\xe6?m&"\xae\xe83\x15k\x8ecwu\xbd\x03\xab\xa9,\xb8\x93\x9eY\\<\x11\xd3 \x04\xd0\xdeb\x88\xf5\xc4\xb20\x92\xd0Cb>\x88W\xab\x90\xaf\x05\x95\xf7\xd1=\x958\x15R{\xca\x87\xbf|\x13\x1a\xbf~\x9c?\xaf\xfaZ%\rJE$\xae%%\xad;\x86=\xb0\xed\xa6\xc8\xa1\x974A.~\xae\n\x95\xd0\xf9\x93!K\xa2J\xf6\xed\xeb\xc6h\xc9\xc0\xa9\xce\x95\xa5\xce\xb4\xed\xe0_\x9d\x1c\x08=\x84}\xb1\xedB\x10\x87Q(\xce\xa6\x1dWC\x82e\xd9m\xf5r\xb5 t\x9b\x04\xc7\xd1~\xd6ew\xc0\xff\x139?\xdbk\x8bV4\xb8\xfd\xad\xb7\xa8JvB\xe6\x08\xdaV\\5n\xa3R\xee\xcf7\xd4Pr\xf8W)7Fp#\xe6\xd7\xed\xcd\'\xbf\xeaf\x92\xb3z[jB\x18d\x0f)`\x99\x8d5\xbeR}\x87Xz\xf38b\x0b\xfd"\x0fo^\xf7\xea\xac\x1e\x07\x8c\x9d\x94\xfff\xb2\xfb!b\x14\xc3\xf3@\xe1\x84\x07\x0e\xad/g|\x03i\xd5\xa8A2*\xdc.\xb8\x1a\x04\'\xb4>\xbd\xc0\x8f\x9b\x82\xbb\x90\x15\'[c\xe8\x90 \xb2\xc1\x05\x98\x97\xab\x03ea\xaf\xdf\xbfBd\x86"QT\x1fmW\xd6\x91\xd5}/\xdb\xef:>\x04\xb2\n\x85\x8aH_\x81\x8a\xc9\x8ddE\x9d\xbb\x8f\x9f\r\x8aj\xb9D\x12\xb9\xbb\'Z\xcd\xc4\xa7=]\x90\xc2\x15\xb5\x8e\x9b\x99f@\x94S\x7f\xd8\xad\xb1w\xbb\xfb\xe8\x01\x03:\x9b\xe5\xa4Y\x1b\x14\xe9\xf2\x97\x9dz\xb6Gg\xb9\n\xb9S\xe8KZ\xe9z\xbc\x90\xe1!0/\x89\xfd\x88Lg\xbc\x1b\xd6\xf7\xdc`3\xf9\xcc\xafz4S\xcd\x05\xe3\xa0t\xe6Ju\xcc\r\xd4\x85\xc2i\xd6eh\xb6\xdb\x02S\x8a\x92\x86\xd7M\xa0\x97\xc0k\x1d\x81\xe6\xe4\xe4\xfc\xbb\xd0\x03I(\x11\xd6\xa9\x17K\xed\x8f\xfbJL\xdd)Pcj\xf05Z\xc3/<\xfa\x05\x14\tu\x0bb\x9e\xc0N\xb9k\x9f&H\xff`l\xc4\x8e\xb8Y]\xa2\x83n0!q\xf6s~zL\xa1\xd3H\x10\xaa\xc6\xfb\xb3\xf8\xaf\x1c\x18+\xf4\xce\xc4\x1a\xf5\xa0\x8f\xd3S\x9c\xc8$D\xbc\x90$\xd2?\xba\xd3c\x10\xd1\x93;C\x8c\x1dY\xc2\xb5Q\xf0\xd4\x98\xae\n\xff\x17\x15"|\xc1\x15\xce(v\xb5\x0c\xddY\n\xac\xb7L\x06\xb1\xa1]\x9c\xe21\x98\x05\xc43\x8e\xf4:\xed!$`V\xc9\x0f\xe0\x9a7F\xac/\x08\xf7S*|\xf7\xa3+k7&4\x0b+\t#Y\xe1\x82\x11NF}\x1fT\xe1\x8a\xcf\xac\xfd\r:(D\xe0\xea\xd6\xdc.$\xf1\xe9rF\xe3\x99\x11$C\xeaE\xf7\x88\x1eiP\x91\x87\xc8\xf4\x8cs\xe6\x83zTx8\xf2\xf0\x10\xe2\xb0\xc8\xd5\xe6\x99*\x04\xe4\xac\xb3W_\xa8s;\xf4\xc0P&\xd1\xee\x14\xa7\xe3\x97/\xd1u\xf7\xef\x8e\xbek\t\x7f{h\xbe\x9b\xbb\xc4q\xaf\xc83r\x1d\x9a\xd3\xd9\xd1\xdc3\xc7\x1e\xad=\xa4\xfc\xac}=WE\x1co\xe1\xad\xc1L\xf2;\xc0[+!\x15\xb7\xa3\x80(o\x0b>\x1dE\xe1ow\xe54\xb7\xa7\x91\x90\tj\xe7\xca\x06\xe5\xe13Z\xe4Hj{\xa2\x7f\xee\xa3H\xa3k\xdb+\xcf\xdbJ\x83m\xc7\\\x1f%L\x00\x9fL\x83\x8b\xf3\xe7\xfb\xfb\xdb\xce[\'o\x00\xb6\xbcmZ\xdf4\t-jv\x17\xf9\xcb>J\xef\x7f\x98q\xf8}\xe8\x9c\xd4z\xa4\x93\xe3\xa3\x9f\x81\x97\x1a\xd3\x12\']\x0b\xcc\x07M\x8d\x05\n1Z\xdf\xfe\xa9\xb9\x00N\xf0\xa6/\x9d\xc7ZH\xef6R\xda\x97B\xc2\x8fK7!\xb4\xa0;\x0c\xf1\xfb\x98A\xe3\xb4:\xe4C\xbe\xfd\x83vf~\x17\xdb\xa6\x9ayTX\xfb\x15\x0fH\xdb)Tp\xc6rKZ\xe2;3\xf6\x7f\xcf.N\x9d!\xcb\xde\x05\xc0\xa3\xee3\xcb\xd5*Y\xbf\xe7@QsW\x07\xcdB\x14}St_C\x14\xa0\x9c\x86\xe5\xe5\x01\x88\xb0\r\xe5\xb1*\x1c\xa0\xa04T\xb3\xe3-\x92w\xab\xf9\xb9\x92\x86t\xd7b\xc6\xf2f\x9e&\xf7\xd5"\xd5_,\x80\xc7\xa1/\xef<\x94\xf7\x0f0\xf8\xab\xec\xa1\xcd\xdb\x18d\x1a,g\x03\xaaX8\xcc~N|\xd16$\xa1t\x98\x0c\x8fT\x0c\xaf\x02?K\x12\xc4\xa4\x91e\x16N\x13r|rv\xf7\xd1Y\x02\xa4\x0f\xff\xac\xc4|"Q\xb0Esz~Lz\xac\xed|\x87b\\\xbf\xd5\xb94U-!\xf7\xf7\x05=\xe13\x91\xc3"\xf9\xe8\xe2\x13\xf2\x19\t\x8ew\x0c\x1d\xcdm\xd9\xf5Y)Y\xeb\x03\xa0\xcf\xd6ya\x1a\x0f\xf0GK$\x1c\xaf\xba\xfa,\xa4\x95\xba\xf8\xa8\x7fPWO\x1a\xbfQ\xd6O\x95\xfc\xbe\t\xb2\xf5\xfbOu\xf2k9q\x7f\xb7\x88\xf4\x9f\xd4\x99\xf9\xaa\xa9\xb1Yo\x98<Z,\x84\x0f2+\x9c\x81\x123\nh\xba\x12\xe8\xfc\xb3\xc2\x0e\xd39Hz\x01r;\x91P\x15I\x8b\xca\x956C\xc8\xf1\xaep\x82\xe62\x8ca\xef\xbe\x92<\x8f\xd1\x1eO2\x90N \xa5\xe8\xff\x96$\x99~0x\x83F\xd2,\xe5\x8b\xd1_"(\x8d\xdd^q11[\x02\x8f\x99\x95>*\xa1\x87\xb2\x19\x18\x9d\x83)r\xf5r\xff\xd5\x8a\tY@\xf6\x0b\xb3\x94\xa83\x05C>\xcf\xb4\x05\x8ew\x16\xaa\xb7\x7f\x80\xbb\xbd\xec\x9fOS9\xdd\x10\xd5\xca,K\x86\xbe\xf9\xd6\x12\xf1\x17U\xf2\x06\xb6\xce\x91\xfa\xf0\xfb&\xe0.\xc3\xf1\xb4\x92\x86U\xa1\x8a\x07/!\x83\x9e;\xe1e\x88N\xce;\xba4x\xc9\xa9\xf7\x81/\x8cx(\xb9\xf7\x857\xbeIw^\xe2D\xce\xe6\xde\x01\xd3$<\x98y\xff\xb5\xcf,r\x13\xd57\x87\x80Wj\x07\xde\xbaM\xea|\xeb\xe3\xdaAq\xc2\xc5\x05`\xfa\x1a\xd7\xf9\xa7\xc5|\xbaH\xe8\xfe\xd3\'}\xb6\xf5\x80Q\xb5\x1e\xe2:\xb2\xf4\xda\x95\\\xd0\xe2_\x94q2\xb9\xcd;\xd2\xd8.]\xc5O\xa64\x04M\xa44\x9c\xbc\xaa\x19\x16]\x19\xcdx\x96/\xdev\xe6\xf4\xdb\xa0\x85\xb5FNR\xdfP:^\xff(&\xcc\xc9V\xe8\\\xb2\x88\xbbr\xa0\xde\xd7\xda\x18\x05}\xe4\x1dcI\x16\xecQ\xcbe\x8f_e\xdc4\x9e\xee=\x80\x8a\xea\xcb\x81\xac\xff\xafJD\xdeN\x95;T\xc3\xac\x00\xe2\x0b\xff\xe2@\x03\x9bs\xb4\x1cC\xaa\x8e\x08\x84\x99\xa2=\xe0\x18\xb1\x97\xc2i\x0e\xd6\x10rr\x90]\x1b\xc3\xa6\xf1\xa0\xeax\xbb\x9b\xa6\x1b> X\x00\x9caG\x88*\x81\xbe\xa2\x9fj\x05\xc6\xabH\xa5\x84"u;\x81>d\xdb\x83L\xbd\'\xb3\x0b\xee\x01\xc1j/Z\xbc\x92\xbb\xfe\x94\x18\xfeU\x86:\xe2\xe0j\x91S#\x1fu\xe8\xd4\x19\x14XUE\xbc\xaf\x06\x9f\x8a\xaaJ7\xc9\xf9\xbax{htT\x91\r;%\x98i0\x05\xacc.5\xd7v\xcf4\x11\x04\xda\x00\x1f\x0e\xb4\x83\n/p\x8d+\x00\x1c\xbbY\xa1\xb8\xfe.L\xa6\x91\x85t\x9b\xc3\xa9\x84\xda\x87\x19\x88 \xb6N\x11d\x9e\xbe\xea\xb5G\x8ec\x15y\x88\x04\xb3\xfa\x7fe\xbb[\x7f<Y\xeb\xa5-*z\x9aV\x17\x8b\xb3\xd4\xf0GB\x9c\xc0\x00\x02\x0eu=8 \xa0!\x04\x1cQ\x0f{\xcd\xb7\xe5\xdb\xd1{\xda\xb6o\xe5\x0fW\xab\xd7I\x98\xba\xd8\xf5\x04\xcc\xdarL5\xcc\xe2\xf9\xe9T7HY\x0b\x9d\xe6\na\x85\xb40\xb4O\xd1\x92:J\xfc~_\x92\x03X2 \xf0@m\xe5\xa0\xbb$\xee\x89\x8b\x92\x9fo\xa7l\xc5\xe0\x17K\xa8R\xa7=k\xc6|hNnw\x18\n\x08\xdeQ\xd5\xe4\x1e0\x8b\xee\xee\x05R&\x91D\xe8\xa6\xda\xe5\x05K_\n\x9e{u1\xe4(Z\xef\xe6\x1d\xe4\xc2\x84\xc5b9\xa4H\xe6\xa7\x03\xf4"\xc6\xec\xd0)\xd9\x1bSd\x9b\x90N}#\x9e;/\x90\xb9Th\xcf\x9e\xc6x;=n4\xf7$\xbc\xb6;\xd6\xf5"\xa8\xd8\xa6\xe2i)&\xaa\x03@\xcf\xb5T%|\x93F\xad-=\xb9y\x96+KZ\xa3q\x04#Y\x8d2\x93\x8aY\xe0\xdb\xcb\xc4S\xc3\xcdz<$\xa8WY5\xa8\x87\x1f\xbcf\x15\xce\xe1\xf2\xd3\xacU\x14R\xa54\xb5g\xcdW\xdc\x19\xeeO4\x84\x18\x17\xe2\xd0mK\x17\x90\xa8\xfa\xa6\x84\x81,\x95-\xd8\xe9\x1b\xc9\x8c\xee\xb9\x87\xaa\xad\xce\x80C\xa4\xfe\xa4\xe5\xc8P\xa5\xcd\xf4\xba\x82\xcd5&\xb0rdh\x184\x8f\xf8\xad\xbe\xc1\xc1OJ\xcc\xbb\r\xc6X@\x8c\xb5smBxw_n\x16\xd6\xf4\x92\xa7\xe6\xc6V\xa48\xa7\x0f\xaf\x1eK\x96\xf0\x0c\xcd\xb1B\\d\xe9\x9c\x1eu\x81\x003\xb4\x85\xd6\xe7\x92\xe7\x15\xa6E\xcb\xf8\xadm9\x9d2r8\xb7\xba\x14\xb6n&\x83\xb2d\xe0uK2Fx\xf1I\xca\xb9p \xd1\xc6P|\xd6\xd5\xd1\xdaYp\x12;\xf9\x87h\xa6\x97\x05\x19\xc8\x92\x0c\xbfB\xe6\xe7+\xfc\xdc\x84\n5\xe0\x848\xb9\x8b\xaf\xcc\xc0\xc2\x1a\xbf\xba\x08G\\3\x8c{\xc5\x0c\xd8\xaaZ?ZM\xf0\'\x98aP\x95\x84\x96\x82qf1\x19\xb5\xd0\x81S\xa9\xbd9m{o+\xfbN/>\xfbC\x1d\xfb\x16\xed\xd1\xbf#\xf9M\xbd\x8b{\xe9N\xfb_\x95\x06\x95\xb3\xe5\x07\x87\x8e\x8e\xf3\x034\xa4\x91g\x15\xce\xb8+\xe4\x03\xf4\xcf\x02Z\xb8\t]oz\xe6\xc0\xc7\x98\xd8\\\x15\xc1\xc4<\xa0-\x91E\x83aRS1\xe3\xf1\x8eH\xb7\x9c\xba\xb4,\xe9\x0c\xc66\x89n\x7f\xc11Q\x8a\x1bK\xee\xb0\xd0\xc1\xcf\xc1\xbd\xa0\x964\xee9\xf0\r\xec\x9ds\x950M\xc7\xf6\xea\x92\x08j`\xabE\xdee\xa4\xcc\x9dy\x02\xe6\xca\xe8\t!\x0b\xc6\x9e\xf2\x12\x1czl\xc0\xe4\xd2\xd3L\xd8\xc8\xe2A\xf8pS\x03+\x8f\x95\xdd\x83\xb9\xee\xc9\xf6\x81\x93J\xdd\xe5\xd1b\xe8\x19\xfd+\xbf\xdb]\xfd\x92F\xe7\x0b\x14\xb5\x9b\x81"\xb9\x99\xb6\xbd\x97\xb3\xc3\xd8\xa2\xb9\x8f1trDXJg(G\xa3\xd8U%n\x8d\x0eWd\x95\x81\x12\xfeTy\x05\xfbrw\xde(\xfe<\xb9\xe8\xee\xa8\xa6\x93\xc9\xae\xd8\x85\x1dx&\x07o3\x0f\xeb:rW\x9e\xb5\x9a\xd6\xcc\xcdOX\xd7\xb2\x91sp\\\x9d\xcd?\xf1\xe9\x89#\xed\xad\xcd?\xff\x83\x84\xa6\x04\xd5\x08C\t\xf3N\x16J\x8d:^\x1d\x1d\x04}\xa3F\xcb\xc7\xa8y\x81\xca\xaf\x8esN\xfcc&^(\xa80\x98\xda\xc8\xaf\xf13\xbeM-\xbfGc%\x8c=\xa0\x19\xcf!F\xb7\xa1\xb6\xe1\x08\x17D\xfc\x92\x9c\xfezy\xceM0\x8chi;\x83\xdbO\x0f\xe8\xbe\xef\xadd\x0cv\xd33X\x11J\xdb[\xb7\xd1\xf5\x11\xd6Q\x914s4\x02\xcfP\xc8|\x00\x00\x8b\xb5\xf1\xf4\xac>\xee\xd4\x00\x01\x88@\xf1?\x00\x00N\xc9\xa8x\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))
except KeyboardInterrupt:
	exit()
