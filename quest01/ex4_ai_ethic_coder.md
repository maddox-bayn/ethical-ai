# Exercise 4: AI as Learning Amplifier
# TOPIC: Wireless routing protocols

# Phase 1: Build Foundation (ME first)

from this topic i learnt that wireless routing protocol are set of rule that determine how wireless devices discover, maintain path and send data between each other
# DIfferaence between proactive  and reactive routing 
proactive routing is also known as table driven it contain a table (database) in (MANETs) mobile ad hoc NETWORK that contain destination address, the next hop, the metric(cost per path), and sequence number, i  it it continousely maintaining updated node to all other node or maintaining an up-to-date map of the entire topology at all time while Reactive is also called on demand, the path are discoverge when needed

# simple scenario design (5–10 devices) with your justification.

# QUESTION:8 wireless sensors in a field some move some are fixed,i ask myself if the device arely send data, should you use proactive or Reactive(answer: reactive) if then now justify "why", "what trade_offs?", "what happens if nodes move frequently", (ANSWER ARE BELOW)
 
If i have 8 wireless sensors scattered across a field and they only blink into life to send data, you are looking at  a sparse, event-driven traffic pattern.in the scenario, sfficency is everything.
# why 
In a proactive protocol (like DSDV or OLSR), every node constantly maintain a complete map of the network. if my 8 sensor only send data once every few hours, a proactive protocol spends 99% of its energy talking about routes that aren't being used.

# the trade-offs: the "First packet"Tax

The Latency Spike (setup Delay):
because the node dosen't know the path beforehand, the very first packet of a transmission cannot be sent immediately. it must wait for a use Route request and for Route reply(RREP)
   result: the first bit of data takes significantly llonger to arrive than subsequent bits
The FLooding Overhead
when a route is needed, the node "screams" to it neighbors to find the destination. this dicovery process uses more instantaneous bandwidth than a single proactive update. in a small network of 8 nodes, this is negligible, but it's the cost of doing business" reactively

# what if nodes move frequently
mobility is the stress test for any routing protocol. if those "some that move" start moving fast or often, the network dynamics shift:
1. rout breakage : in a reactive system, a moving node will frequently walk out of range of its next hop. this break the ctive path
2. the Error-Discovery loop: Every time a link break, the source node must perform a route error (RERR) notificationand then restart the entire discovery process.
3. Trpping point: if nodes move too fast, the protocop spends more energy trying to find routes than it does actually sending data. this is known as high control overhead
# trask reflection
my 8 node field, reactive remain the winner because the "rarely send data" constraint is the biggest factor. the cost of number of nodes matter so for this task even with frequent movement, the cost of proactive update for 8 nodes that aren't even talking is usually higher than the cost of fixing a broken route on the fly.

# Phase 2: Strategic AI Use
# Test your understanding, explore edge cases with targeted questions, then validate.
1. What are failure scenarios of AODV in high-mobility environment:
In high-mobility environments, AODV often fails not because it can't find a route, but because it can't find one fast enough to keep up with physical movement.

    The "Route Staleness" Lag: By the time a Route Reply (RREP) travels back from the destination to your moving sensor, the intermediate nodes may have already moved out of range. The source thinks it has a path, but the "bridge" is already gone.

    Broadcast Storms: If multiple nodes move and break links simultaneously, every node starts "screaming" Route Requests (RREQ) at once. In a small 8-node field, this is okay, but in larger fields, this congests the entire frequency.

    The RERR Loop: AODV spends so much time sending Route Error (RERR) messages and restarting discoveries that the actual data packets stay stuck in the buffer until they time out.
2. How does OLSRhandle tpoplogy changes:
OLSR: How it Handles Topology Changes

OLSR (Optimized Link State Routing) is proactive. It doesn't wait for a problem; it tries to predict the map of the field constantly using MPRs (Multi-Point Relays).

    Periodic Hello Messages: Every node sends a "Hello" packet at set intervals (e.g., every 2 seconds). If a sensor moves and a neighbor stops hearing its "Hello," the neighbor immediately marks that link as dead.

    MPR Flooding: Instead of every node broadcasting changes, only specific "elected" nodes (MPRs) announce topology updates. This makes OLSR much faster at updating the "map" than traditional proactive protocols.

    The High-Mobility Cost: If your sensors move faster than the "Hello" interval (e.g., they zip across the field in 1 second), OLSR will be routing data based on a map that is 2 seconds old. You get routing loops or black holes where data is sent to where a node used to be.
3. what happen when packet los occures?:
The impact of a lost packet depends entirely on what was lost:
The "Real Understanding" Summary

    AODV fails because it is reactive—it's always one step behind a fast-moving target.

    OLSR handles changes better by being proactive, but it eats battery life constantly to keep its map fresh.

    Packet Loss in a moving field usually signals a Link Break, which forces the protocol to consume even more energy to "re-map" the field.

Since you're working on a Go-based backend project, would you like to see how you'd structure a simple "Health Check" or "Heartbeat" logic in Go to simulate these 'Hello' messages for your sensors?