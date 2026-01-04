device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print(f"High Temperature alert!")
    else:
        print(f"tempertaure is normal!")    
else:
    print(f"Device is offline!")