import time
import momo_engine
incoming_payloads = [
    {"id": 101, "reference": "  s4  fEes  "},
    {"id": 102, "reference": "momo.sch transfer"},
    {"id": 103, "reference": "Pocket money deposit"},
    {"id": 104, "reference": None},
    {"id": 105, "reference": "   FEES si admission  "}
]
print(" Starting Zapier live simulator Automatio  process...")
start_clock = time.time()

for payload in incoming_payloads:
    print(f"\n[Processing Item ID: {payload['id']}]")

    try:
        raw_ref = payload["reference"]

        clean_ref, routing_target = momo_engine.process_transaction(raw_ref)

        print(f"Clean data: {clean_ref}")
        print(f"System Route: sending funds to -> {routing_target}")
    except Exception as error_message:
        print(f"CRITICAL ERROR SKIPPED: Could not process ID: {payload['id']}")
        print(f"Reason: {error_message}")

    end_clock = time.time()
    latency = end_clock - start_clock
    print("\n=============================================")
    print(f"Automation pipeline finished in {latency:.6f} seconds!")
    print("================================================")