# lamports_clock
Implementation of Lamport Clock in Python
Lamport's logical clock is a mechanism to order events in a distributed system. Here's a Python implementation

Explanation:
Local Event: A simple increment of the clock.
Send Event: Increments the clock and sends its value with the message.
Receive Event: Updates the local clock to be one more than the maximum of its own clock and the received clock.

How It Works:
Each simulated process (process_a and process_b) runs independently using its own instance of the LamportClock class.
Events like sending, receiving, or local actions update their respective clocks.
Messages are represented by the clock value being passed between simulated processes.
