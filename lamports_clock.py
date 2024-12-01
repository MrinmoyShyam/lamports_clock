class LamportClock:
    def __init__(self, process_name):
        self.time = 0
        self.process_name = process_name

    def local_event(self):
        """Increment clock for a local event."""
        self.time += 1
        print(f"{self.process_name} - Local event: {self.time}")

    def send_event(self):
        """
        Increment clock for a send event.
        The sender's clock value is sent along with the message.
        """
        self.time += 1
        print(f"{self.process_name} - Send event: {self.time}")
        return self.time

    def receive_event(self, received_time):
        """
        Update clock on receiving a message.
        Synchronize with the received clock and increment.
        """
        self.time = max(self.time, received_time) + 1
        print(f"{self.process_name} - Receive event. Updated clock: {self.time}")


# Simulation of two processes on one device
if __name__ == "__main__":
    # Simulating Process A
    process_a = LamportClock("Process A")

    # Simulating Process B
    process_b = LamportClock("Process B")

    # Process A local event
    process_a.local_event()

    # Process A sends a message to Process B
    sent_time = process_a.send_event()

    # Process B receives the message from Process A
    process_b.receive_event(sent_time)

    # Process B performs a local event
    process_b.local_event()

    # Process B sends a message to Process A
    sent_time = process_b.send_event()

    # Process A receives the message from Process B
    process_a.receive_event(sent_time)
