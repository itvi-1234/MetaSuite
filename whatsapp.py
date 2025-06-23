import uiautomator2 as u2
import time
import random

def connect_device():
    d = u2.connect()
    print(f"[✓] Connected to device: {d.device_info.get('model', 'Unknown')}")
    return d

def select_whatsapp():
    print("\n1. WhatsApp\n2. WhatsApp Business")
    pkg = input("Select app [1/2]: ").strip()
    return {
        "1": "com.whatsapp",
        "2": "com.whatsapp.w4b"
    }.get(pkg, "com.whatsapp")

def human_delay(min_sec=2.5, max_sec=4.0):
    time.sleep(random.uniform(min_sec, max_sec))

def firstclick(d):

    d.click(305 , 488)

def close(d, pkg):

    human_delay(2.5, 4)  # Longer delay before closing
    d.app_stop(pkg)
    human_delay(3, 4)
    d.press("home")
    print("[✓] WhatsApp closed successfully")

# 1. Send message to a single number
def send_to_single_contact(d, pkg):
    d.app_start(pkg)

    human_delay()

    numbers_input = input("Enter numbers (comma separated): ")
    message = input("Enter message: ").strip()

    numbers = [num.strip() for num in numbers_input.split(",")]

    first_number = numbers[0].strip()

    for number in numbers:
        full_number = f"91{number}" 

        print(f"\n[→] Sending to {full_number}")
        d(resourceId="com.whatsapp:id/search_bar_inner_layout").click_exists(timeout=5)
        human_delay()

        d.send_keys(full_number)
        human_delay()

        if number == first_number:
            d.click(1038, 513)  # Adjust as per screen resoltion
        else:
            d.click(280 , 680)  # Adjust as per screen resoltion
        human_delay()

        d(resourceId="com.whatsapp:id/entry").click_exists(timeout=5)
        d.send_keys(message)
        human_delay()

        d(resourceId="com.whatsapp:id/send").click()
        print(f"[✓] Message sent to {number}")
        human_delay()

        d(resourceId="com.whatsapp:id/whatsapp_toolbar_home").click_exists(timeout=5)
        human_delay()


# 2. Send message to a group
def send_to_groups(d, pkg):

    d.app_start(pkg)

    groups_input = input("Enter group names (comma separated): ").strip()
    message = input("Enter message to send: ").strip()

    group_names = [name.strip() for name in groups_input.split(",")]

    for group in group_names:

        print(f"\n[→] Sending to group: {group}")

        d(resourceId="com.whatsapp:id/search_bar_inner_layout").click_exists(timeout=5)

        human_delay()

        d.send_keys(group)

        human_delay()

        d.click(750 , 700)

        human_delay()

        d(resourceId="com.whatsapp:id/entry").click()

        d.send_keys(message)

        human_delay()

        d(resourceId="com.whatsapp:id/send").click()
        
        print(f"[✓] Message sent to group '{group}'")
    
        human_delay()  

        d(resourceId="com.whatsapp:id/whatsapp_toolbar_home").click_exists(timeout=5)

        human_delay()

#7 forwarding images to targets
def forward_image_to_targets(d, pkg):

    d.app_start(pkg)

    human_delay()

    source_contact = input("Enter contact / group with the image: ").strip()
    recipients = input("Enter recipients (comma separated): ").strip()
    recipient_list = [r.strip() for r in recipients.split(",")]

    print(f"[→] Searching for source contact: {source_contact}")

    d(resourceId="com.whatsapp:id/search_bar_inner_layout").click_exists(timeout=5)
    human_delay()
    d.send_keys(source_contact)
    human_delay()
    d.click(1038, 513)  # Adjust based on resolution
    human_delay()

    print("Clicking forward button")
    d(resourceId="com.whatsapp:id/action_button").click_exists(timeout=5) 
    human_delay()

    add_caption = input("Do you want to add a message with the image? [y/n]: ").strip().lower()

    if add_caption == "y":
        caption = input("Enter your message: ").strip()
        d(resourceId="com.whatsapp:id/appended_message_container").click_exists(timeout=5)
        d.send_keys(caption)
        human_delay()

    for recipient in recipient_list:
        print(f"[→] Selecting recipient: {recipient}")

        d(resourceId="com.whatsapp:id/menuitem_search").click_exists(timeout=5)

        human_delay()

        d.send_keys(recipient)
        human_delay()

        d.click(1038, 513)  # Adjust as per screen resolution
        human_delay()

        d(resourceId="com.whatsapp:id/back").click_exists(timeout=5)

        human_delay()
    
    d(resourceId="com.whatsapp:id/send").click_exists(timeout=5)

    print("[→] Sending forwarded image...")
    
    print("[✓] Image forwarded successfully to selected contacts/groups.")
    human_delay()
    d(resourceId="com.whatsapp:id/whatsapp_toolbar_home").click_exists(timeout=5)


# 3. Create new group
def create_group(d, pkg):

    d.app_start(pkg)
    members = input("Enter phone numbers (comma separated): ").split(",")
    group_name = input("Enter new group name: ")

    human_delay()

    d(resourceId = "com.whatsapp:id/fab").click_exists(timeout=5)

    human_delay()

    d.click(575 , 386) # adjust as per screen resolution

    first_number = members[0].strip()

    human_delay()

    d(resourceId="com.whatsapp:id/menuitem_search").click_exists(timeout=5)

    human_delay()

    d.send_keys(first_number)

    human_delay()

    d.click(305 , 488) # adjust as per screen resolution(first member)

    human_delay()

    for number in members[1:]:

        d(resourceId = "com.whatsapp:id/menuitem_search").click_exists(timeout=5)

        human_delay()

        d.send_keys(number.strip())

        time.sleep(5)

        d.click(580 , 650) # adjust as per screen resolution

        human_delay()
    
    human_delay()

    d(resourceId = "com.whatsapp:id/next_btn").click_exists(timeout=5)

    human_delay(3 , 4)

    d(resourceId = "com.whatsapp:id/group_name").click_exists(timeout=5)

    human_delay()

    d.send_keys(group_name)

    human_delay()

    d(resourceId = "com.whatsapp:id/ok_btn").click_exists(timeout=5)

    time.sleep(5)

    d(resourceId = "android:id/button1").click_exists(timeout=5)

    human_delay()

    d(resourceId = "com.whatsapp:id/send").click_exists(timeout=5)

    print("[✓] Group created successfully!")

    human_delay()

    d(resourceId="com.whatsapp:id/whatsapp_toolbar_home").click_exists(timeout=5)

# 4. Create a broadcast and send message
def create_broadcast(d, pkg):

    d.app_start(pkg)

    members = input("Enter phone numbers (comma separated): ").split(",")

    human_delay()

    first_number = members[0].strip()

    d(resourceId = "com.whatsapp:id/fab").click_exists(timeout=5)

    human_delay()

    d(resourceId="com.whatsapp:id/menuitem_search").click_exists(timeout=5)

    human_delay()

    d.send_keys(first_number)

    time.sleep(1.5)

    human_delay()

    d.swipe(1038, 513, 1038, 513, 1.8)

    d(resourceId="com.whatsapp:id/menuitem_new_broadcast").click_exists(timeout=5)

    human_delay()

    d(resourceId="com.whatsapp:id/menuitem_search").click_exists(timeout=5)

    human_delay()

    d.send_keys(members[1].strip())

    time.sleep(1.5)

    human_delay()

    d.click(260 , 580)

    human_delay()

    for number in members[2:]:

        d(resourceId = "com.whatsapp:id/menuitem_search").click_exists(timeout=5)

        human_delay()

        d.send_keys(number.strip())

        human_delay()

        d.click(260 , 650) # adjust as per screen resolution

        human_delay()
    
    d(resourceId="com.whatsapp:id/next_btn").click_exists(timeout=5)

    human_delay()

    d.click(250 , 190) #touch the broadcast name 

    human_delay()

    d(resourceId="com.whatsapp:id/menuitem_overflow").click_exists(timeout=5)

    human_delay()

    add_caption = input("Do you want to add broadcast name [y/n]: ").strip().lower()

    if add_caption == "y":
        caption = input("Enter the name: ").strip()

        d(resourceId="com.whatsapp:id/appended_message_container").click_exists(timeout=5)

        human_delay()

        d.click(670 , 520)

        human_delay()

        d.send_keys(caption)

        human_delay()

        d(resourceId="com.whatsapp:id/ok_btn").click_exists(timeout=5)

    print("[✓] Broadcast created successfully !!")

    d(resourceId="com.whatsapp:id/whatsapp_toolbar_home").click_exists(timeout=5)

# 5. Post a status from contact image
def post_status(d, pkg):

    d.app_start(pkg)

    number = input("Enter target whose image to use: ")

    human_delay()
    
    d(resourceId="com.whatsapp:id/search_bar_inner_layout").click_exists(timeout=5)

    human_delay()

    d.send_keys(number)

    human_delay()

    d.click(1038 , 513)

    time.sleep(2)

    d.long_click(650 , 1750) #long clicking the last image 

    human_delay()

    d.click(880 , 180) # clicking on forwward button

    human_delay()

    d.click(254 , 375) # To click add status

    add_caption = input("Do you want to add a message with the image? [y/n]: ").strip().lower()

    if add_caption == "y":
        caption = input("Enter your message: ").strip()
        d(resourceId="com.whatsapp:id/appended_message_container").click_exists(timeout=5)
        d.send_keys(caption)
        human_delay()
    
    human_delay()

    d(resourceId="com.whatsapp:id/send").click_exists(timeout=5)

    # Navigate to contact image, open it, save it, and post as status (simplified placeholder)
    print("[•] Grabbing image placeholder and posting status...")
    # Complex image extraction automation can go here

    print("[✓] Status posted (simulated).")

# 6. Create a community
def create_community(d, pkg):

    d.app_start(pkg)

    caption = input("Enter the name of the community: ").strip()

    human_delay()

    d(resourceId = "com.whatsapp:id/fab").click_exists(timeout=5)

    human_delay()

    d.click(300 , 800) # new community coords

    human_delay()

    d(resourceId = "com.whatsapp:id/community_nux_next_button").click_exists(timeout=5)

    human_delay()

    d.send_keys(caption)

    human_delay()

    d(resourceId="com.whatsapp:id/new_community_next_button").click_exists(timeout=5)

    time.sleep(5)

    d(resourceId="com.whatsapp:id/community_navigation_add_group_button").click_exists(timeout=5)

    human_delay()

    d.click(316 , 560)

    human_delay()

    group_input = input("Enter existing group names to add (comma separated): ").strip()
    group_names = [g.strip() for g in group_input.split(",")]

    for group in group_names:

        print(f"[→] Adding group: {group}")

        d(resourceId="com.whatsapp:id/menuitem_search").click_exists(timeout=5)

        human_delay()

        d.send_keys(group)
        human_delay()

        d.click(350 , 680) # adjust as per screen resolution(group name)

        human_delay()

        d(resourceId="com.whatsapp:id/back").click_exists(timeout=5)

    human_delay()

    d(resourceId="com.whatsapp:id/next_btn").click_exists(timeout=5)

    time.sleep(5)

    d(resourceId="com.whatsapp:id/review_groups_permissions_confirm_button").click_exists(timeout=5)

    print("[✓] Community created successfully !!")

# Main loop
def main():
    d = connect_device()
    pkg = select_whatsapp()

    while True:
        print("\n📱 WhatsApp Automation Console")
        print("1. Send message to single number")
        print("2. Send message to a group")
        print("3. Create a group")
        print("4. Create broadcast and send message")
        print("5. Post a status from contact image")
        print("6. Create a community")
        print("7. Forward image to target")
        print("0. Exit")

        choice = input("Choose an option [0-7]: ").strip()

        if choice == "1":
            send_to_single_contact(d, pkg)
        elif choice == "2":
            send_to_groups(d, pkg)
        elif choice == "3":
            create_group(d, pkg)
        elif choice == "4":
            create_broadcast(d, pkg)
        elif choice == "5":
            post_status(d, pkg)
        elif choice == "6":
            create_community(d, pkg)
        elif choice == "7":
            forward_image_to_targets(d, pkg)
        elif choice == "0":
            print("👋 Exiting automation tool.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
