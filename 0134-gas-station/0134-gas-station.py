class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        if sum(gas) < sum(cost):
            return -1
        
        total_surplus = 0
        start_station = 0
        curr_surplus = 0

        for i in range(len(gas)):
            net_gas = gas[i] - cost[i]
            total_surplus += net_gas
            curr_surplus += net_gas

            if curr_surplus < 0:
                curr_surplus = 0
                start_station = i + 1
        
        if total_surplus < 0:
            return -1
        
        return start_station