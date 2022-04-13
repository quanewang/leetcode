a="time awscurl -X POST http://internal-EcsSe-LoadB-1382OGLD5RPJB-1541769330.us-west-2.elb.amazonaws.com/ -d '{ \"Operation\": \"com.amazon.quanwanecspoc3#CreateBeer\",  \"Service\": \"com.amazon.quanwanecspoc3#QuanwanEcsPoc3\",  \"Input\": { \"Beer\":{\"beerId\": \"beerid6\", \"name\": \"name6\"}  }  }'"
a="time awscurl -X POST http://internal-EcsSe-LoadB-1382OGLD5RPJB-1541769330.us-west-2.elb.amazonaws.com/ -d '{     \"Operation\": \"com.amazon.quanwanecspoc3#GetAllBeers\",     \"Service\": \"com.amazon.quanwanecspoc3#QuanwanEcsPoc3\",     \"Input\": {     } }'"

for i in range(1, 100):
  print(a)