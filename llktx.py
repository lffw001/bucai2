import datetime

import requests, logging
import json, sys, time, os
from notify import send

# 1.3修复闯关任务不跑
# 乐乐看提现（配合蛋姨的本），变量名:lelekck，需要抓包apillk.cengaw.cn/请求头里面的device#Authorization，（Authorization只需要Bearer后面的部分）
# 6.22新增看资讯任务和闯关,多号换行隔开,ua换成自己的（User-Agent）
# 需要提5块设一次定时弄在任务本前面
# 一天运行2-3次
# cron 0 0,7,15 * * *
money = "5"  # 提现金额，默认5
ua = "Dalvik/2.1.0 (Linux; U; Android 11; V2055B Build/TP1A.2224.014)"

# Make Sure You're Running The Program With python3.10 Otherwise It May Crash
# To Check Your Python Version Run "python -V" Command
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SY\x8a\xa6\xfd=\x00\x05b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf4\x7f\xff\xff\xbf\xfb\xf7\xff\xff\x80@\x00\x18?\xe0\xce\x92\xe0\nq\xf0z\x01\xa3-\xbbv\xe9\xc2\x87\x18u\xc0\xea\x05\x8cn\xc3\x87\rM&\x99\t\xa0j\x9f\xa9\xa9\x8c\xa9\xec\xa6\xd2zH\xf2jm\xa4\xf4jM\x1e)\xea~\x08\x91\xfaMC\xd3(\xfdSe\x07\xa9\x90\xfdM\'\xeab\x83\xc8F\xd4\xd3\'\xa9\xa1\xb4\xd4hz\x8fQ\x90\x00\x00\x00\xf5\x00i\xea4\xf3T\x1a@\x80\x02i\xa0M\xa9\x84d\xc9\x82\x13\x1a\x9a2\x9bSd\x9az\x13jzM\x1e\xa0\x00\xd1\xa0\xd0\x06\x86\x80444\x01\xa1\x90\x1a\x00\x00\x00\x00\x00\x00\x83@\xd0\x0c\x83 \xd04\r\x18\x99\x1a\x06\x80\x0c@\x06\x81\x844h\x1a\x00\x00\x00h\x0c\x8d\x1a\x00\x00\x00\x01\xa3#&LM\x00\xc9\xa3\x06\x93 \x9a\xa7\xa1\xa9\x0f)\xea=CF\x83\xd4\xd0\x004\x1a\x00\x00\x00\x01\xa0\x00\x06\x80\x1a\x00\x00\x00\x03\xd4\x00\x00\x00\x00\x00\x00\x00\x83@\xd0\x0c\x83 \xd04\r\x18\x99\x1a\x06\x80\x0c@\x06\x81\x844h\x1a\x00\x00\x00h\x0c\x8d\x1a\x00\x00\x00\x01\xa3#&LM\x00\xc9\xa3\x04\x89 L\x9a\t\x89\x1e\x81\xa21\x02\x8f)\x90m\x0c\xa3i\xa9\xb2\x8c\x0c\xa7\xa9\xa3@z\x804\x00\r\x07\xa8\xc9\xeamM\xa2i\xe9\xa9\xa0\r\x01\x90\xd3@\x06\x80z\x86\x8c\x81\xb2\x9a~\xa7@\xdd\x04\xa1\x04r3F\xac\xe2Y3\xe2d\xb7\xaa=\x12\xab^\x9a\xf1\xa0:\xea\xc7\xbb\x836\x1b\'\x9e\xc4\xa8g\x98\x80T\xd9\x94\xca\xa1U,"\xc3*\xc5g\x10\xac\x15\x92@\x9b]\xc8vO\x98h\n2}g\x8a8\xed\xd7\x9bB\x8d1E20\xa9,\xa1\xa9\xb0dF\xfa\x93V\xf6#\xf7\x0c\xfe&,J\xb2\xe2A\t\xc6 Ds\x9c\x88\x11y\x8d$\r\x84%A\x06F-6%\xeaF#\xdb\xae\xde#\xbb!\xb3xf#\xb1;\xae\x1fBn\xdf\xc2\xe4W\x86\xb6\xc9\x82\x18\x8a\x08I;\x9fw,\xc8S\x18\x06\x83\xc5`\nM"zj\x86\xefN7 \x98\x16\x1f\x85\x86\x94\x83:\xe5\x8c\x00\xea\xb6#\x8f\xc0\xb9\xe0^Z\rP\xe1\xa0 m\xb4\xc39\x9d\xed\xad\r\x8d4\x93\r:4i\x82\x01\xa8`\x044u\x9a}c\xdfI\xed\x9e\xfb\x89H\x1c.,"\xe5{\xd1\xd9/E4\xc5u\x0c\xd8q\x98\xa5\xa4\n\xb0\xaeB1\xad\x08W\xe8Ms\xccu#D\x94c\x8f\xf9\x11HI\xae\x02l\xb0E\xc6l:\x0f\x0f^\x81\x15E\x14\x9d\x83K\x0ev\x0bk\xae\xbf\x8eBJk+6\r\x83\x97\xcbwudl\xe7\x96\x9bu\xbf\xe1\xeaO2\x016\xc2\xe6\x84\x12\x91\x97_h\xa3\x7f\xa8e\xae\x9a\x0e\x8c\xfd\x1e\x8d\x17-\xcca\xd1\xef\xf3iO\xf2\x1fT6\x99\xb6s\xe6\x1e\xb3\x14\xbb\xce\xb6\x9b\x94!y\xfa\xb4\x0c\xda\xafW\x9aK\x99\x97?\x16\x0c\xeeW\xd5X\\\xdb\xa7\x9cD\xd4\x14\xb9\xc3\x06E"p\xc5\xb2g\x1e\xaf\x1e\xc3F(\x0f3nVaL\xbc\x9eM\xac\x18Y2M\x0c\x1d\xf56%v\xf1\xaf\xa5UT\x10\xd85\n\x1d\xd6-,U$h\xe8\xc7\xb0\xbbM\xc6\xed\xc1"M\xf6\xd6\x99b\x94\x15\xd6X\xcc\xf5\x8a\xab\xb5\xdd.\xcae4\x83kUE\x88\xeb\x9cmT-\xab\xd9\xf2\xafV\x1ds\xba\x93-\xd089/\x94\xe1J\x87,6\xdf\x1a\xdd\xc4%\x84\xe7\xbbo\xf9\xe20m\xb0%z\xe5\xb1\xf8\x02\x8b\xe4\x91T\xf8H\xcaJ\xd8\xb8+\xf2\x88q\xb4\x8e0!\x92\'\xd9t\xcf\x12\\l[\xa7c1\x86a\x04\x03&\x04\xcc\xc7\xc8i\xca<\x86^\x08\x04\x0f\xd28\xaaz.\xac\x8ey\xee\x19\x1c3R\x9c\xa55w\x94\xcaveU\x9c\x1a\xd5u\x94\xd2SJ\x81C\x14\xa6\xa0\xa9\xd8\xc8\xc1=\x1f\xf6\xa8E\xfa\xca\xe5@\xb6\xd3\xd1!M5\xf5?M\x9dn\tofEu\x8a\xbb\x8bY\xdc\'\x9cS\xcc\xb8\xf4\xf5\x14P*(T\xd7)\x81\xcc\xa7\x90\xa5%\n\x01\xa8Hd\x91\xd7\x13\x18\xc0\xb2D2\xf1\xd0\x8b\xb65\x99\xdae\x07\xbf\x9f<\xd7\x07\x84(k\xd2\xde\x03\xe0P64O\xae&5A\xad@\x94@\x88:S\x1bV`\x04\x03\x89\xea\x02\x02d\x16{\\9\xfad\x92r\xaa\x0e\xb0,J\xd0\x1a\x0cN\xf4\xcb\x17\xc6w\xbeW\x7f)\x9e\xefg\xd2\xfb\xefy\xe3\xd1\xa1{\x04^w\xf4\xa4\xa7\xd0iA\x93\xc4A\'\x88\xc8\xcfc^\x0b\xe3\xcfQ \xa4\x0e\xf8\xf3\xf8f\x0eA\xe5C\xc2\xe1\xb6U\x9c\x9b?\t\x14 \xd1"p\x14\xe5O\xc4\xd6\xae*\xc2L\xa8\x9dRh\x025\xd6Sh\x81fA\x1d<\x99\xcc\\sj\xa3G7\x04[\x92p1\x05\xca\xee\xba\x95\xb0$\n\xe2\xc4\x87\xa3\xe5s!r\xd4\xd3\xb6\x8f\x96\x1fD\x97\xfap\xeeQ*G\x9a\xffE\xcea,\xee\x9c\xbd\xf6o\x05i&\x82I\xe4\xa9.\x99\x88>0\x136\xf0\xe0#6 %pPR\x91\x14\x14\xf1\xa2\xb0\x02q\xa5\xb7]\xaa\x03\xb2\x9d\x8a\xcb\x1c\xac-\xc6c\xb6\x0br\xe8\xd5v\xe5\x9b\xeb\xaaS\xde\xccsL\x16g\xe1\xa4\x9a\xab\x1db\xb8\x1c\t\x0fR\x90\x13\x8da\x1d\xd4\xc8J\x83\'$nB\t\x19\x90\xc1!tV(\x1aYj\xd2\xc7R\x98\x06\xe1\xd2Q\xa3\x14\xc3\xbd\x9d\xc6\x81V\xda;z\xd92\x07>\xdca\x88\xf0\xc3 \x80\xde\x85s\n]pL\xd3\xcb\xceY\xbd\x0ek\x0bK\xc4\xc0E4>4\x04s\x84\xfc>\xd5\x1dH\t\xea\xca\xe8\xe5\xa54\x82P\xbc\xcb\xad\x9es\xaa\xb1, \x94\xaf\x8d9\xb0\xfbM\x93F#w/\x9bo\x92.6\xbc\xfb\x87\x1a\xb8\x18K\x95\x03\x043f\xf1v\x0e\x87\x89\xb0c\n\xd2\xb7\x9a\x9c\xfe\x08\xaa\xec\x90\xdd\xd3\xd1\xcb\x8e\x86\xc7!\x1bP\xfebw\x13&4\xfbN\xb6\x94Za\x96\x1e8|\xf4T\xe2\x9e\xa6\x89 \x94 \x96\xb6\xb5hV\x87\x91\x86\x16EW@x9\x84zX\xae\x05&q\xdf:UB\x9a\xe3#y\x90V\xaf[[\xb3N2\x95kL\xeaN\xd4\x1e\xd6\xd9\xab\xe6\x12\xa6X\x98m\xa7\t}&\t\xb7\xb9\x04\x0c\x102\xb8\xe3\xa1\xba\x94\xaaVYj\xf7+\xed\xd9\x97n\x98\xbf\xb8>>f\x8e\x13\x1a\xa8[f\xd2\x9f\xf6\xdaZ[\xb1"\xcd\xfcv\xdbl\xf7\x17\xc9\xbe\xb8;\xdaf\xe5Dm\xd4m\xc7B[g\xfa\xbfY\xd2\x18\x199\x17\xa8\xdew\xb7\xc5\xd0E\x00\xd5\xe9\x18\x1c\x8cE=($\x03\xa3e\xd5L\x9a-e\x8b\t\xb4\x144\x16|\xcd\xcfB\x0cs\x9fc\xd5b\x8dLl\xe3\xce\xbeKc^8-KN\xa0];\xcf\xbc\x05\x9c~\xd5\xd2&\xddk\x97\xb8\x9c\xa3\xb0\xd6\x91\xb2\x0b\xb1N^\x0c\x8el\xc0+\x83z\xd6\xb8Jz\x19\xad6r\x14\x0c\x94\x18g3eb\'\x97i\x9a\xbb\x9dL9S\xa5\x9d\x88\xe1\xc1i.\xd2\xa1\x13\x0c\xd1ln3\x15\\\x8aq`\xadi\xeb\x17R\x06\xc2\xbb \x06$\x94x\x10\x94\xc5\x8bB\xbb\xd3\x1b\x9c\'\x03\x9e\x07\x12t\x03\x042A\x92\xb2Z\xc0\xac\x96\x08e\x0c@%]\x0c\xe7\xf7|\xaf\x997?\x9d\xc3\xaf\xc0\xef\xbb\xe1X+\x05`\xb9\xea\xcf\x9e@]\x13W.kAf\xd4\xee\x14\xfcw\xf0\xf9\xa0\x18\xed\x86\xdb\xde\xebM7\xd1\x17\x172\xc3\xda\xeaV\x96\xa5^\x0c\xbe\xcd\x95\xe4\x98\x95\x1e\x8e7\xf2\x89\xa1\xab\x8b\x8d\xd8\xfb\xd9PNQ\x18Gf2c\x7f\xb9\xe2\xd12\xaa!\x9e\x0c\xe1\xbc\xf4\x9cN#<\xe6E\xd5\xa3-&\xe4\xf7\xe5\x87.j\xe1Q\xd9Ph\xf0F\xdaU\x07\xd0\xcb\xd1\xb5\n\xed\xd5\x16\xb3\x06\xbe\xb5\\h\xc7\xcc\x91\xaf\xe4\xef1\xa3R\xfe\xea\xde\r\xc6\rZ\x16ObA\x01\xc7z\xcas\xa6\x18\xc7\x06\x9c\r_mnA}\xbd\xee\xda\xf4\x84\xc9\xadM\xe2\r\xdfw\x93\xce\xb7\xd3\xe0\xd9\xfa^\x04@k\x12ez\xdez\xac\xbdD\x06W\xba\xc2\xc9\xee\xa3*5\x0f#R\x0e\xa7\x0b\x8d\x15\x9e\xdb=\xe4\x9eG\x8b\x97\xc5\xca\xf0\xf3F\x0e\xfd\xec7$tsbt \xb3\x97\xc3\x07\xdf\x98\xd1*T\x81\x95}\x8a\x8e\xf1\x91\x9a\xb1\xf2\x9b9\xea\x18\xd0\xde\x00\xbbgR\x88\xa9C\x84!\xaa{\x8a\x97M\x13@[\x1e\n:\x8e\x02\'\xc6\xd2\x84\xd1\x87\xbc\xce\x06\xbaB8^`N\xe2\x8b\xa1M4\xf9\xe3\x0b<h+\xb3\x9b\x8f\x80\xf6Z\x95K?\x80Y\x04\x1c\x84w\x94P\x00\xcc\xc8\x84\x06\x1d5\xd4\x04\xaa\x02S\x1e\x8a\xdb\xbdV\xc2)F\x83\xf1Mpk\xaf\xd2\xa67\xd4h\x82\xdbI#\xd0/\x83\x1e\x86\xc7\x8f\xd2\xa0\xdbC\x0c\x16\x07;\x97\x9cpj\x13\xa9\xed\xe7a\x85mo\x0c\x01q\xf2\xaa\xd5\x04\x94\x02\xd9\xedW\x96E\x86\xd0i\x86\xa6\xd5\xde\x858\xac\x9d\x9b!\xa3\x0c\x08X\x0c\x02\xb0\xa4\xa2\x92\xf5\xb8\xa4[\xbdL\xf3\x9eR\xf5-\xd4\xaa,\xe1\xdbRA\xd0d\x03\xd6\x0c\xd3ke\x04\xe3?[\x7f\x80\x80s\x18\xc9\xcfnq\x16\xbfi\x8c-\x1e\x9e\x14k\xce\xce\\\x05\x8c\x0fH\x81\xad\xe7\xe2n\xac\xa5\xfbT\xcdY\x98\xdb\xbf\xafb\xc2\xd9\xae\x14\x92\xc8\xb5\xab\x91C\x0bTQ\x05\xe0p\xfd\xd6$\x97\xb0\xb0(\xa2\xc5\x0b\x13\x1c\x07\xbbA\x0e\x07"\xdec\xc6\xb2\xd2\xa3\xc5\x03\x9b0\x15\x01,\xb1\xe6\n(R\x93\x80\xdf\x1a\x98\xbbv\x0f\x82\xf6KA\xa9\xd2\xa8t\xf0g\xe1H\x8dr\'\ri\x81\xc3rL\xc3\x82]L\xd4\x03.\xbb\xbd>\xcd\xcd\x96\x8c V0\x17P\xa2pY^\xe4\xfe\xe5c\x03)b]\xbc<Q\x8f\x9f\x12\x83\xad\x12\xee\xbb\x13\xf11u\xf4O\xed4\x90\xb4\xab1\xf5z[4\x1b\x1b\xbb\xc9]0x\x9a\xa6\xb0e\xe1m\xb6j&\xa0\xb1\xadJ\xa9\x9ec+\xa5\xa4T\xce\xe6\xfdRf\xe8\xed\xa4\xb7\xacH\xa9\x8a\xb3\x90\xe4\x1b\x86\xadR\x80f|\xaf\xe0\xc9Ax\x8d\xf6\x8c\xb7Iq\'{;\x9c\xddo\x1c\x1c\xd7\xc4\xcc\x13\xe8f\xbb}\x06lT\xb1\xe7\x81l\xed\xb66\xc7\x0e\xe2]?\'ov\xf4<D\xd0\xadw\xac\xb3?r;V\x9eIjM\x8f,JW63\xec\xbck\xe4j)\xb8K\x16\xe1N\x13\x8eC\x94\xc1<\x04\xb1\xb8z\xb8\xe4\xf8\xd91UUKy\x8e\xe7\xbf\xb7\x0e\xcb\x02\x0b\xfeh\x06Y\\k\xb9w8\xf3\xaa\xfe5\xba\x17:\xad\xa1\xfc\xb9\x856F\xb7\xf7\x9a\xbf\xc7S|\xa7\xe3\xa8\x80\xc5\x8c\xa9\x83F$\x03\xea\xac\x13\x84B\x91\r\xcc\x1aL\'\x00l$b\x7fQ\xac\x04y-\xe1\x1d"\xabX\x8a\x92\xf0\x01\x8d\xbd\x99\xb9\x9e\xd8\xc5\x83\xa0/-\x9b\xaf]\xcbYk\x13F\xc7\x86q\x04\x9c\xa3\x16\xd3\xf1\xb3M\xf3\xb5\xd6V\x9dp\x98Q\xd9\xdd5-\xa0\x87\xf4wP\x84[\x19\x05E\'\xea\x1e\x9c?y\xb8#\x9f\xfd\x1e\xb86\xbe\xb1\x86\xae\x91\xa5 j\x06\x9a\xb8x\xb0\xbf\x18\xf94\x07*\xdc\xe9-&C\x17Z\t\xa9\x16\x93\xf50\x99G\xd8\xa8\xe2\xdbR\xe9\t\xdb}\x83\x03\xcf\xff:#\xf6\x8f\xf0\xb9S.\x91\xfb\xb5\x95a\xad\x10\xc1\x87\x96p<j\xdd.\x18\xfe\xe6\xea\x92\x14v\xa3\x0e\xe8>"\xb0\xde*\xd4Z\x96\x88\xb1I\x05\x81\xa6\xb4v^\xabR\x19\x99\x84\x99\xfb\xe8?\'\x96H\xfeiA\x94\x82o\xbc\xad]\x1d/\x18\x88\xc1K }!y\x13\xe5Kc\xd7xX\x8e\x7f\xd6\xd3\x91\xb5Lf\xf2\xc8\x1bT\xc4#\xd2\xf3\x8b\x7f\xeaT!$b\xf7^\xe8/`o\xb5\x11\xe8\x18\x85\'\xd9o\xedP\xacm\x0e\x07\x83\xc0\x8b?\x82\xb5\x83R"\xd6\x88\xb3CGn\xd4\x08\xad$t(\x01\x9e\xb8n\xa9\xe8\rF3\xc0\x0e\xb6&\xaaa#\x92*9e\xd8\xfb\xf5v{\xa8\xf0\xe298\xa0\xf1\x11\x9e\xc2|x\xf9\xbc\xe3\xc5\x9cm\xf9\xbe\x85gi\xd7\xf0\xc3\\\xe57\xc0\xdc0\xeb\x03\xb2\x1f\xec{\xcf\'\xfd?"(\xe9\x17WP\xbb\x03\x8d\xd4\xf3\x8d\x82XU\xa6\x15\xd9\xe1\xac\xb0\xed\x19\x84\x8f\xd6u\xff\x03\xc7\xc8\x97\x95\xe4\xccz\xd6\xd5h\xad\xd4;\x07P\xaer&_\xf8!0\xc83\t69\x18\x9a\xd1\xd4S\xa3\xccB\xa6\'\xe8@\xad\x16n\x9b\x97\xb9\xd4\xec\xb9\x9a\xb2\xee\x0e\xf6\\\xd6\x11-\xc9\xdd\x9e\x85\xf2tAr\xd8\xbb\x9e\xc2\xe5\x03\x8f\xe2+\xd8O \xcc\xa0\xe4\xc1\x14\xa7|\xc7X\x1cD\xe7x+b\xec\xb8E\t\xecm\xf0\x1c?;Aw\x10{\x93w\xe5=e\xbak\xda\xa2H \xd0\x1a\xcc\xaef\xc54\xf2\x85\xb8\xbb#lSm:\xa6\xe9]\xc0n\xb0&\xf0\x1b\xbe\xeb\xc2CJ|2\xca\xac-}c56!(C\xa2\x1c\x82\xc6\xcd\xc5\xb1\x11\xb4\x94\'E0\x11\x17V\xc3\xfa\xabok\x8f\xf9\x1d\xda\xc0P\xc6pz\x1b\x84]1U#\xe4\x8ed\x97\x16\xach\x0bm p\x11\x1c\x90\x9b(FT"qk^Z#0R\xb2\xdbo\x96;\xf3\xff\xedS\x18\x1b#(d\x82\xef\xeb?\x1ek\xe6_\xba`\xbf\xf1w$S\x85\t\x08\xaao\xd3\xd0')))
except KeyboardInterrupt:
	exit()
