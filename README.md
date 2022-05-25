git add .; git commit -m . -a;git push origin

git remote set-url origin git@github.com:quanewang/leetcode.git

practice
* https://leetcode.com/
* https://www.hackerrank.com/
* https://www.geeksforgeeks.org
* https://www.interviewbit.com/
* https://codedrills.io


mock
* https://www.pramp.com

problems
* https://leetcode.com/problemset/all/?difficulty=HARD&page=1
* https://www.careercup.com/page?pid=google-interview-questions



https://leetcode.com/problems/container-with-most-water/
https://leetcode.com/problems/jump-game/

```
Given a positive sorted array a = [ 3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21 ];
Define a function f(a, x) that returns x, the next smallest number, or -1 for errors.
i.e.
f(a, 12) = 12
f(a, 13) = 12
```

{
  "Resources": {
    "rrplinkAlbE4013A08": {
      "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
      "Properties": {
        "LoadBalancerAttributes": [
          {
            "Key": "deletion_protection.enabled",
            "Value": "false"
          },
          {
            "Key": "proxy_protocol_v2.enabled",
            "Value": "true"
          }
        ],
        "Name": "rr-plink-Alb-alpha--iad",
        "Scheme": "internal",
        "SecurityGroups": ["sg-864f22f8"],
        "Subnets": ["subnet-468d093f", "subnet-f2c563b9"],
        "Type": "application"
      }
    },
    "rrplinkAlbrrplinkAlbListenerFDF7C62F": {
      "Type": "AWS::ElasticLoadBalancingV2::Listener",
      "Properties": {
        "DefaultActions": [
          {
            "TargetGroupArn": {
              "Ref": "rrplinkAlbtg63C57CE8"
            },
            "Type": "forward"
          }
        ],
        "LoadBalancerArn": {
          "Ref": "rrplinkAlbE4013A08"
        },
        "Certificates": [
          {
            "CertificateArn": "arn:aws:acm:us-west-2:109239231449:certificate/c9efc01e-2686-4f08-b371-a8efda6945f3"
          }
        ],
        "Port": 443,
        "Protocol": "HTTPS",
        "SslPolicy": "ELBSecurityPolicy-TLS-1-2-Ext-2018-06"
      }
    },
    "rrplinkAlbtg63C57CE8": {
      "Type": "AWS::ElasticLoadBalancingV2::TargetGroup",
      "Properties": {
        "HealthCheckIntervalSeconds": 10,
        "HealthCheckPath": "/sping",
        "HealthCheckPort": "traffic-port",
        "HealthCheckProtocol": "HTTPS",
        "Name": "rr-plink-Alb-tg-alpha--iad",
        "Port": 443,
        "Protocol": "HTTPS",
        "TargetGroupAttributes": [
          {
            "Key": "stickiness.enabled",
            "Value": "false"
          }
        ],
        "Targets": [
          {
            "AvailabilityZone": "us-west-2a",
            "Id": "172.31.45.137",
            "Port": 443
          }
        ],
        "TargetType": "ip",
        "VpcId": "vpc-62b6ee1b"
      }
    }
  }
}