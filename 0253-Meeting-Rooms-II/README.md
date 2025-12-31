<h2><a href="https://leetcode.com/problems/meeting-rooms-ii">253. Meeting Rooms II</a></h2><h3>Medium</h3><hr><p>Given an array of meeting time interval objects consisting of start and end times <code>[[start_1,end_1],[start_2,end_2],...] (start_i < end_i)</code>, find the minimum number of rooms required to schedule all meetings without any conflicts.</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [(0,40),(5,10),(15,20)]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Explanation:
room1: (0,40)
room2: (5,10),(15,20)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [(4,9)]
<strong>Output:</strong> 1
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 <= intervals.length <= 500</code></li>
	<li><code>0 <= intervals[i].start < intervals[i].end <= 1,000,000</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>You should aim for a solution with <code>O(nlogn)</code> time and <code>O(n)</code> space, where n is the size of the input array.<font face="monospace">&nbsp;</font>
