from django.shortcuts import render
from datetime import datetime

def engtv(request, tvno='0'):
    tv_list = [{'name':'SkyNews', 'tvcode':'9Auq9mYxFEE'},
               {'name':'Al Jazeera', 'tvcode':'-upyPouRrB8'},
               {'name':'French 24', 'tvcode':'HeTWwH1a0CQ'},
               {'name':'DW News', 'tvcode':'qMtcWqCL_UQ'},]
	now = datetime.now()
	tvno = tvno
	tv = tv_list[int(tvno)]
	return render(request, 'engtv.html', locals())

