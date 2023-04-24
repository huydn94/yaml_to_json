import ruamel.yaml as yaml
import json

if __name__== "__main__":
    print("Lam viec voi file yaml")
    with open ("user.yaml", "r") as stream :
        user_yaml= yaml.safe_load(stream)
    print("Print type of user_yaml")
    print(type(user_yaml))
    print("---------------")
    for key in user_yaml:
        print(key)
    print("---------------")   
    print("print value of key 'id'")
    print(user_yaml['id'])    
    #{key:{key1:value1},}
    user_json= json.dumps(user_yaml, default=str, indent=4)
    print("Structure JSON")
    print(user_json)
    file=open("user.json","w")
    file.write(user_json)
    file.close