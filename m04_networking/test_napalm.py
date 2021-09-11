import napalm
import json

def main():
    driver_ios = napalm.get_network_driver("AOS-CX")

    ios_router = driver_ios(
        hostname="192.168.188.42",
        username="n1mbu5",
        password="n3tw0rks"
    )

    print("Connecting to IOS Device...")
    ios_router.open()
    print("Checking IOS Device Connection Status:")
    print(ios_router.is_alive())

    print(json.dumps(ios_router.get_interfaces(), sort_keys=True, indent=4))

    ios_router.close()
    print("Test Completed")

if __name__ == "__main__":
    main()