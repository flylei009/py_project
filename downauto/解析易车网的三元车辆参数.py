# -*- coding:utf-8 -*-
import json
carCompareList = [[["143938","1.5T 手动 豪华型","https://img1.bitautoimg.com/autoalbum/files/20200827/375/20200827103954395475422_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["10.69万","无","","3年或10万公里","1.5","涡轮增压","","6","手动","","5","9","2020","SUV","汽油"],["4670","1865","1700","2710","1580","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手动","6","","","6.6","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"],["无","无","无","有","无","无","无","有","有","无","无","无","无","有","后方影像","有","无"],["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"],["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","无","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["143939","1.5T 手自一体 精英型","https://img1.bitautoimg.com/autoalbum/files/20200827/375/20200827103954395475422_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["11.49万","无","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2020","SUV","汽油"],["4690","1865","1700","2710","1585","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"],["无","无","无","有","无","无","无","有","有","有","无","无","无","有","后方影像","有","无"],["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"],["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","无","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","无","无","无","无","蓝牙,wifi","USB","无","无","2-4","无","无","12.3","无","有","有"]],[["143644","1.5T 手自一体 豪华型","https://img1.bitautoimg.com/autoalbum/files/20200826/937/20200826095754575410405_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["12.49万","无","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2020","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["定速巡航","无","无","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","无","有","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["143645","1.5T 手自一体 尊贵型","https://img4.bitautoimg.com/autoalbum/files/20200821/943/20200821232138213877181_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["13.19万","无","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2020","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","有"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","有","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","有","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["143940","2.0T 手自一体 领航型","https://img1.bitautoimg.com/autoalbum/files/20200827/375/20200827103954395475422_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["13.99万","无","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2020","SUV","汽油"],["4700","1865","1710","2710","1670","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","有","无","无"],["皮质","有","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["143646","2.0T 手自一体 旗舰型","https://img1.bitautoimg.com/autoalbum/files/20200824/762/2020082412024224218534_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["15.49万","无","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2020","SUV","汽油"],["4700","1865","1710","2710","1725","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","有","有","有","有","无","有","有","有","有","无","无","有","有","360度全景摄像","有","有"],["LED","有","自动开闭,自动远近光,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜记忆,后视镜加热","","有","无","有","无","无","感应雨刷","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","有","有","皮质","有","上下调节,前后调节","无","无","双温区自动空调","手动空调","无","有","无","无"],["皮质","有","带记忆电动调节","电动调节","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","加热","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","有","无","无","蓝牙,wifi","USB,SD卡槽","无","无","7-8","无","无","12.3","有","有","有"]],[["137073","1.5T 手动 豪华型","https://img3.bitautoimg.com/autoalbum/files/20200709/738/202007091874_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["10.69万","10.68-10.69万","","3年或10万公里","1.5","涡轮增压","","6","手动","","5","9","2019","SUV","汽油"],["4670","1865","1700","2710","1580","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手动","6","","","6.6","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"],["无","无","无","有","无","无","无","有","有","无","无","无","无","有","后方影像","有","无"],["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"],["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["137074","1.5T 手自一体 精英型","https://img3.bitautoimg.com/autoalbum/files/20200116/328/20200116943_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["11.49万","11.49-11.49万","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2019","SUV","汽油"],["4690","1865","1700","2710","1585","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"],["无","无","无","有","无","无","无","有","有","有","无","无","无","有","后方影像","有","无"],["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"],["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","2-4","无","无","12.3","无","有","有"]],[["136682","1.5T 手自一体 豪华型","https://img2.bitautoimg.com/autoalbum/files/20190903/576/2019090316021921936323_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["12.49万","12.49-12.49万","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2019","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["定速巡航","无","无","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","无","有","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["136681","1.5T 手自一体 尊贵型","https://img3.bitautoimg.com/autoalbum/files/20190827/094/20190827095707577164583_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["13.19万","13.19-13.19万","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2019","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","有"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["136680","2.0T 手自一体 领航型","https://img4.bitautoimg.com/autoalbum/files/20191028/629/20191028921_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["13.99万","13.99-13.99万","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2019","SUV","汽油"],["4700","1865","1710","2710","1670","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","有","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]],[["133063","2.0T 手自一体 旗舰型","https://img3.bitautoimg.com/autoalbum/files/20191219/216/201912191025_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["15.49万","15.49-15.49万","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2019","SUV","汽油"],["4700","1865","1710","2710","1725","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","有","有","有","无","有","无","有","有","有","无","无","有","有","360度全景摄像","有","有"],["LED","有","自动开闭,自动远近光,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜记忆,后视镜加热","","有","无","无","无","无","感应雨刷","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","有","有","皮质","有","上下调节,前后调节","无","无","双温区自动空调","手动空调","无","有","无","无"],["皮质","有","带记忆电动调节","电动调节","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","加热","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","7-8","无","无","12.3","有","有","有"]]]
print(type(carCompareList))

print(carCompareList[0])
print(carCompareList[0][0])
print(carCompareList[0][1])
print(carCompareList[0][2])
print(carCompareList[0][3])
print(carCompareList[0][4])
print(carCompareList[0][5])

baseInfoList = {
    'specId': carCompareList[0][0][0],     #车型ID
    'specName': carCompareList[0][0][1],    #车型名称
    'specImg': carCompareList[0][0][2],    #车型图片
    'seriesId': carCompareList[0][0][3],     #车系ID
    'seriesName': carCompareList[0][0][4],     #车系名称1
    'seriesName2': carCompareList[0][0][5],     #车系名称2
    'seriesName3': carCompareList[0][0][6],     #车系名称3
    'year': carCompareList[0][0][7],         #哪年款
    'productNow': carCompareList[0][0][8],      #在产
    'saleNow': carCompareList[0][0][9],      #在销售
    'null_1': carCompareList[0][0][10],      #未知
    'bbs': carCompareList[0][0][11], #汽车论坛
    'bodyType1': carCompareList[0][0][12], #车身别  紧凑型SUV
    'bodyType2': carCompareList[0][1][13], #车身型号  SUV
    'colors': carCompareList[0][0][13], #车身颜色
# ["11.49万","无","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2020","SUV","汽油"]

    'price': carCompareList[0][1][0],  #厂家报价
    'dealerPrice': carCompareList[0][1][1],  #商家报价
    'saleDate': carCompareList[0][1][12] +'/'+carCompareList[0][1][11] +'/'+carCompareList[0][1][10],    #上市时间
    'engineType': carCompareList[0][1][14],    #动力类型
    'engine': carCompareList[0][3][1] +' '+  carCompareList[0][3][7] + carCompareList[0][3][8] +'缸 '+carCompareList[0][3][9],    #发动机
    'maxPower': carCompareList[0][3][2]+'kW/'+carCompareList[0][3][3]+'N.m',    #最大功率
    'gearboxType': carCompareList[0][3][15] + '挡 ' + carCompareList[0][3][14],   # 变速箱类型
    'oilConsumption': carCompareList[0][3][18],   # 油耗
    'environmental ': carCompareList[0][3][19],   # 环保标准
    'warranty ': carCompareList[0][2][11],   # 保修政策

# TODO 把剩下的参数设置成字典值

}
print(baseInfoList)



"""
[
	[
		["143939","1.5T 手自一体 精英型","https://img1.bitautoimg.com/autoalbum/files/20200827/375/20200827103954395475422_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"]
		,["11.49万","无","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2020","SUV","汽油"]
	       ,["4690","1865","1700","2710","1585","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"]
	       ,["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""]
	       ,["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""]
	       ,["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"]
	       ,["无","无","无","有","无","无","无","有","有","有","无","无","无","有","后方影像","有","无"]
	       ,["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","无钥匙启动","远程启动","无","无","无","无"]
	       ,["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"]
	       ,["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","无","无","按比例放倒","无","无"]
	       ,["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","无","无","无","无","蓝牙,wifi","USB","无","无","2-4","无","无","12.3","无","有","有"]
	  ],

	  [["143938","1.5T 手动 豪华型","https://img1.bitautoimg.com/autoalbum/files/20200827/375/20200827103954395475422_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["10.69万","无","","3年或10万公里","1.5","涡轮增压","","6","手动","","5","9","2020","SUV","汽油"],["4670","1865","1700","2710","1580","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手动","6","","","6.6","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"],["无","无","无","有","无","无","无","有","有","无","无","无","无","有","后方影像","有","无"],["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"],["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","无","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]] 	 ,[["143644","1.5T 手自一体 豪华型","https://img1.bitautoimg.com/autoalbum/files/20200826/937/20200826095754575410405_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["12.49万","无","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2020","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["定速巡航","无","无","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","无","有","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]]	 ,[["143645","1.5T 手自一体 尊贵型","https://img4.bitautoimg.com/autoalbum/files/20200821/943/20200821232138213877181_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["13.19万","无","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2020","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","有"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","有","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","有","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]]	 ,[["143940","2.0T 手自一体 领航型","https://img1.bitautoimg.com/autoalbum/files/20200827/375/20200827103954395475422_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["13.99万","无","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2020","SUV","汽油"],["4700","1865","1710","2710","1670","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","有","无","无"],["皮质","有","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]]	 ,[["143646","2.0T 手自一体 旗舰型","https://img1.bitautoimg.com/autoalbum/files/20200824/762/2020082412024224218534_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2021","在产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|原子灰,#46556b|安第斯灰,#585b62|大地棕,#5c3724|炫晶白,#ffffff"],["15.49万","无","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2020","SUV","汽油"],["4700","1865","1710","2710","1725","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","","210"],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","有","有","有","有","无","有","有","有","有","无","无","有","有","360度全景摄像","有","有"],["LED","有","自动开闭,自动远近光,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜记忆,后视镜加热","","有","无","有","无","无","感应雨刷","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","有","有","皮质","有","上下调节,前后调节","无","无","双温区自动空调","手动空调","无","有","无","无"],["皮质","有","带记忆电动调节","电动调节","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","加热","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","有","无","无","蓝牙,wifi","USB,SD卡槽","无","无","7-8","无","无","12.3","有","有","有"]]	 ,[["137073","1.5T 手动 豪华型","https://img3.bitautoimg.com/autoalbum/files/20200709/738/202007091874_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["10.69万","10.68-10.69万","","3年或10万公里","1.5","涡轮增压","","6","手动","","5","9","2019","SUV","汽油"],["4670","1865","1700","2710","1580","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手动","6","","","6.6","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"],["无","无","无","有","无","无","无","有","有","无","无","无","无","有","后方影像","有","无"],["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"],["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]]	 ,[["137074","1.5T 手自一体 精英型","https://img3.bitautoimg.com/autoalbum/files/20200116/328/20200116943_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["11.49万","11.49-11.49万","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2019","SUV","汽油"],["4690","1865","1700","2710","1585","5","620","58.0","225/65 R17","225/65 R17","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","无","无","无","无","有","无","有"],["无","无","无","有","无","无","无","有","有","有","无","无","无","有","后方影像","有","无"],["卤素","有","自动开闭","无","高度调节","单天窗","有","有","电动调节","","无","无","无","无","无","有","后雨刷","无","无","无","无","遥控中控","无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","手动空调","手动空调","无","无","无","无"],["皮质","无","无","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","2-4","无","无","12.3","无","有","有"]]	 ,[["136682","1.5T 手自一体 豪华型","https://img2.bitautoimg.com/autoalbum/files/20190903/576/2019090316021921936323_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["12.49万","12.49-12.49万","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2019","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["定速巡航","无","无","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","无","有","遥控中控","智能进入,无钥匙启动","远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","无","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]]	 ,[["136681","1.5T 手自一体 尊贵型","https://img3.bitautoimg.com/autoalbum/files/20190827/094/20190827095707577164583_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["13.19万","13.19-13.19万","","3年或10万公里","1.5","涡轮增压","","6","手自一体","","5","9","2019","SUV","汽油"],["4690","1865","1710","2710","1625","5","620","58.0","225/60 R18","225/60 R18","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1499","1.5","131","178","5500","265","1450-4500","直列","4","涡轮增压","直喷","","92号","无","手自一体","6","","","6.7","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","有"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","无","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]]	 ,[["136680","2.0T 手自一体 领航型","https://img4.bitautoimg.com/autoalbum/files/20191028/629/20191028921_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["13.99万","13.99-13.99万","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2019","SUV","汽油"],["4700","1865","1710","2710","1670","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","无","有","有","无","无","无","有","有","有","无","无","无","有","360度全景摄像","有","无"],["LED","有","自动开闭,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜加热","","无","无","无","无","无","有","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","无","有","皮质","有","上下调节,前后调节","无","无","自动空调","手动空调","无","无","无","无"],["皮质","有","电动调节","无","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","无","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","5-6","无","无","12.3","无","有","有"]]	 ,[["133063","2.0T 手自一体 旗舰型","https://img3.bitautoimg.com/autoalbum/files/20191219/216/201912191025_2.jpg","5665","长安CS75 PLUS","长安CS75 PLUS","changancs75plus","2020","停产","在销","","http://baa.bitauto.com/","紧凑型SUV","尊贵黑,#000000|星际蓝,#003598|安第斯灰,#585b62|大地棕,#5c3724|炫动红,#9e0f0f|炫晶白,#ffffff"],["15.49万","15.49-15.49万","","3年或10万公里","2.0","涡轮增压","","8","手自一体","","5","9","2019","SUV","汽油"],["4700","1865","1710","2710","1725","5","620","58.0","225/55 R19","225/55 R19","非全尺寸","3年或10万公里","","","","","","","","1450","","","",""],["1998","2.0","171","233","5500","360","1750-3500","直列","4","涡轮增压","直喷","","92号","有","手自一体","8","","","8.1","国六","","","","","","","","","","","","","","","","","","",""],["前轮驱动","麦弗逊式独立悬架","多连杆式独立悬架","无","通风盘","盘式","电子驻车","承载式","无","","","","","","","","","","",""],["有","有","有","有","有","有","有","无","有","有","无","无","无","有","无","有"],["ACC自适应巡航","有","有","有","无","有","无","有","有","有","无","无","有","有","360度全景摄像","有","有"],["LED","有","自动开闭,自动远近光,转向辅助灯","有","高度调节","全景天窗","有","有","电动调节,电动折叠,后视镜记忆,后视镜加热","","有","无","无","无","无","感应雨刷","后雨刷","无","无","电动开合","有","遥控中控","智能进入,无钥匙启动","远程解锁,远程通风,远程启动","无","无","无","无"],["塑料,皮质","有","有","皮质","有","上下调节,前后调节","无","无","双温区自动空调","手动空调","无","有","无","无"],["皮质","有","带记忆电动调节","电动调节","靠背调节,高低调节,前后调节","靠背调节,前后调节","无","靠背调节","加热","无","有","有","无","按比例放倒","有","无"],["触控式液晶屏","有","有","无","GPS导航,实时路况,在线地图","有","智能语音控制","手机互联","无","无","无","蓝牙,wifi","USB","无","无","7-8","无","无","12.3","有","有","有"]]]
"""