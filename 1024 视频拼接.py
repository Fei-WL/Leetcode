from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # min_num = 0
        # max_num = T
        # result = []
        #
        # while len(clips) != 0:
        #     point = 0
        #     temp_min = len(clips)
        #     temp_max = len(clips) + 1
        #     while point < len(clips):
        #         if clips[point][0] <= min_num:
        #             if temp_min == len(clips):
        #                 temp_min = point
        #             elif clips[temp_min][1] < clips[point][1]:
        #                 temp_min = point
        #
        #         if clips[point][1] >= max_num:
        #             if temp_max == len(clips) + 1:
        #                 temp_max = point
        #             elif clips[temp_max][0] > clips[point][0]:
        #                 temp_max = point
        #
        #         if temp_min == temp_max:
        #             break
        #
        #         point += 1
        #
        #     if temp_min == len(clips) or temp_max == len(clips) + 1:
        #         return -1
        #
        #     if temp_min == temp_max:
        #         result.append(temp_max)
        #         print(clips[temp_max])
        #         return len(result)
        #
        #     else:
        #         min_num = clips[temp_min][1]
        #         max_num = clips[temp_max][0]
        #         if min_num > max_num:
        #             result.append(temp_min)
        #             result.append(temp_max)
        #             return len(result)
        #         print(clips[temp_min], clips[temp_max])
        #         if temp_min < temp_max:
        #             clips.pop(temp_max)
        #             clips.pop(temp_min)
        #         else:
        #             clips.pop(temp_min)
        #             clips.pop(temp_max)
        #
        #         result.append(temp_min)
        #         result.append(temp_max)
        #
        # return -1

        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)

        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last

        return ret

clips = [[0,5],[1,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],
         [8,13],[9,14],[10,15],[11,16],[12,17],[13,18],[14,19],
         [15,20],[16,21],[17,22],[18,23],[19,24],[20,25],[21,26],
         [22,27],[23,28],[24,29],[25,30],[26,31],[27,32],[28,33],
         [29,34],[30,35],[31,36],[32,37],[33,38],[34,39],[35,40],
         [36,41],[37,42],[38,43],[39,44],[40,45],[41,46],[42,47],
         [43,48],[44,49],[45,50],[46,51],[47,52],[48,53],[49,54]]
T = 50
print(Solution().videoStitching(clips, T))
