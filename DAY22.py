normal_queue = ["101", "102", "103"]

vip_queue = ["VIP201", "VIP202"]

print("Initial Queues")
print("VIP Queue:", vip_queue)
print("Normal Queue:", normal_queue)

print("\nProcessing Visitors...\n")


while vip_queue or normal_queue:
    if vip_queue:
        visitor = vip_queue.pop(0)
    else:
        visitor = normal_queue.pop(0)

    print("Processed:", visitor)

    print("Remaining VIP Queue:", vip_queue)
    print("Remaining Normal Queue:", normal_queue)
    print("-" * 40)