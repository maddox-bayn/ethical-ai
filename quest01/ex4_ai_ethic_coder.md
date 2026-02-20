# Exercise 4: AI as Learning Amplifier
# TOPIC: Wireless routing protocols

# Phase 1: Build Foundation (ME first)

from this topic i learnt that wireless routing protocol are set of rule that determine how wireless devices discover, maintain path and send data between each other
# DIfferaence between proactive  and reactive routing 
proactive routing is also known as table driven it contain a table (database) in (MANETs) mobile ad hoc NETWORK that contain destination address, the next hop, the metric(cost per path), and sequence number, it continousely maintaining updated node to all other node or maintaining an up-to-date map of the entire topology at all time while Reactive is also called on demand, the path are discoverge when needed

# simple scenario design (5–10 devices) with your justification.

# QUESTION:8 wireless sensors in a field some move some are fixed,i ask myself if the device arely send data, should you use proactive or Reactive(answer: reactive) if then now justify "why", "what trade_offs?", "what happens if nodes move frequently", (ANSWER ARE BELOW)
 
If i have 8 wireless sensors scattered across a field and they only blink into life to send data, you are looking at  a sparse, event-driven traffic pattern.in th scenario, sfficency is everything.
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
# task reflection
my 8 node field, reactive remain the winner because the "rarely send data" constraint is the biggest factor. the cost of number of nodes matter so for this task even with frequent movement, the cost of proactive update for 8 nodes that aren't even talking is usually higher than the cost of fixing a broken route on the fly.

# Phase 2: Strategic AI Use(used AI)
# Test your understanding, explore edge cases with targeted questions, then validate.
1. What are failure scenarios of AODV in high-mobility environment:
In high-mobility environments, AODV often fails not because it can't find a route, but because it can't find one fast enough to keep up with physical movement.

    The "Route Staleness" Lag: By the time a Route Reply (RREP) travels back from the destination to your moving sensor, the intermediate nodes may have already moved out of range. The source thinks it has a path, but the "bridge" is already gone.

    Broadcast Storms: If multiple nodes move and break links simultaneously, every node starts "screaming" Route Requests (RREQ) at once. In a small 8-node field, this is okay, but in larger fields, this congests the entire frequency.

    The RERR Loop: AODV spends so much time sending Route Error (RERR) messages and restarting discoveries that the actual data packets stay stuck in the buffer until they time out.
2. How does OLSR handle tpoplogy changes:
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

# Phase 3: Real Application
# Design a small smart-city network (1,000 IoT sensors, 50 traffic lights, 10 emergency vehicles). Decide protocols, justify choices, list failure points, then refine with AI feedback.

# my attempt on soving this:
|Device               |Protocol           | justification                 |failure points | 
|---------------------|-------------------|-------------------------------|---------------|
|1,000 IoT Sensors    |Reactive routing   |energy efficient,              |high mobility  |
|50 traffic light     |Proactive routing  |fast response needed,          |energy drinage |
|10 emergency vehicles |Reactive routing   |Avoid maintaining full topology|mubility disruption|

# AI feedback and reviews
1️⃣ IoT Sensors (1,000 nodes)

You chose: Reactive routing
Justification: Energy efficient
Failure risk: High mobility

✅ What’s Correct

Reactive is better than proactive for large networks.

Energy efficiency is a valid reason.

⚠️ What Needs Correction

Failure risk: High mobility — this is incorrect.

IoT sensors are typically:

Static

Fixed position

Mobility is NOT the main risk here.

Better failure risks:

Battery depletion

Network congestion (1,000 nodes sending at once)

Gateway overload

Packet collisions

Scalability bottlenecks

Now we’re thinking realistically.

🔍 Improve Your Justification

“Energy efficient” is too shallow.

Stronger justification:

Reactive routing reduces continuous control message exchanges, lowering bandwidth and energy usage in large-scale low-power sensor networks.

See the difference?

More precise. More defensible.

2️⃣ Traffic Lights (50 nodes)

You chose: Proactive routing
Justification: Fast response needed
Failure risk: Energy drainage (batteries)

✅ What’s Correct

Fast response — good reasoning.

⚠️ Major Issue

Traffic lights are NOT battery-powered.

They are connected to city power infrastructure.

Energy drainage is not the main failure risk.

Better risks:

Central controller failure

Network partition

Cyberattack

Software malfunction

Latency spikes

Think contextually.

🔍 Improve Justification

Why proactive?

Because:

Small network size

Stable topology

Precomputed routes reduce latency

Reliable coordination between nodes

That’s layered reasoning.

3️⃣ Emergency Vehicles (10 nodes)

You chose: Reactive routing
Justification: Avoid maintaining full topology
Failure risk: Mobility disruption

✅ This is mostly correct.

Now deepen it.

Emergency vehicles require:

Ultra-low latency

High reliability

Rapid topology adaptation

Reactive routing helps because:
Routes are discovered dynamically when vehicles move.

But here’s something deeper:

Pure reactive may introduce initial delay during route discovery.

So what might be better?

Hybrid routing.

Predefine zones for city regions (proactive locally), reactive across zones.

Now you’re thinking architect-level.

🚨 Let’s Upgrade Your Architecture

Right now your thinking is per-layer isolated.

Real smart-city networks are hierarchical.

Better structure:

IoT Sensors → Local Aggregators → Core Network
Traffic Lights → Regional Control Nodes → Core
Emergency Vehicles → Direct priority channel to traffic control

Now routing isn’t just protocol choice — it’s topology design.
# AI ANswer of Task!

| Device                    | Routing / Protocol Choice                                      | Strong Justification                                                                                         | Major Failure Points                                                              |
| ------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **1,000 IoT Sensors**     | Reactive routing (e.g., on-demand mesh)                        | Minimizes control overhead and reduces energy use in large-scale low-power static deployments                | Battery depletion, gateway overload, packet collisions, congestion bursts         |
| **50 Traffic Lights**     | Proactive routing                                              | Small, stable network with fixed topology; precomputed routes ensure low-latency coordination                | Controller failure, network partition, cyberattack, software faults               |
| **10 Emergency Vehicles** | Hybrid routing (Proactive within zones, Reactive across zones) | Vehicles are mobile and require ultra-low latency; hybrid ensures fast local response and dynamic adaptation | Mobility-induced route breaks, initial route discovery delay, signal interference |

# Reflection
**% human judgment vs. AI contribution:**the percentage of contribution of this task is a will be 40% / 60%: at first i learn through documentation i grew more knowledge about this concept but i still more confusion, then i improved my understanding using AI, AI contribution was 60%
**Could you defend decisions without AI?:**if i am to defind the decision of this project without AI i would do so because i have agood understandin of the basic.
**What will you still remember in 6 months?:**IN the interval of 6 month i will still remember about system and how to think in system not just basic of concept but the why and how the things flow.
**Did AI make you sharper, or think for you?:**Yes in this project AI made me sharper, it did not think foe me but it refined my view it should cases i missed point i omited, and how system works.