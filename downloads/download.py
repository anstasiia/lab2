import urllib2

area = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
       '22','23','24','25','26','27']

for x in area:
    url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+ x +".txt"
    vhi_url = urllib2.urlopen(url)

    out = open(x +'.csv','wb')
    out.write(vhi_url.read())
    out.close()
    print "VHI id"+ x +" is downloaded..."
