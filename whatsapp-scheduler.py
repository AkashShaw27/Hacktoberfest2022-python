"""
Author - Richmond Nyamekye

install requirements: python -m pip install pywhatkit

Schedule a whatsapp message to be sent at your convenience

"""
import pywhatkit


def send_msg(phone: str, msg: str, hour: int, minute: int) -> None:
    pywhatkit.sendwhatmsg(phone, msg, hour, minute)


def send_whatmsg_to_group(group: str, msg: str, hour: int, minute: int) -> None:
    pywhatkit.sendwhatmsg_to_group(group, msg, hour, minute)


def main():
    msg_type = int(input("Enter 1 to send a message to a USER and 2 to a GROUP: "))
    if msg_type == 1:
        phone = input("Enter phone number: ")
        # make changes to suit your needs
        if phone[0] == "0":
            phone = phone[1::]
        while True:
            if len(phone) < 9:
                raise ValueError("Invalid phone number: ")
            else:
                break
        phone = f"+233{phone}"
    elif msg_type == 2:
        group = input("Enter group to send message: ")
    msg = str(input("Enter message: "))
    hour = int(input("Enter the time in hour: "))
    minute = int(input("Enter the time in minute: "))

    if msg_type == 1:
        send_msg(phone, msg, hour, minute)
    elif msg_type == 2:
        send_whatmsg_to_group(group, msg, hour, minute)


if __name__ == "__main__":
    main()
