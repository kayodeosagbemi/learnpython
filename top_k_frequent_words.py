from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #create a dictionary called historgram
        histogram = dict()
        for word in words:
            if word not in histogram:
                histogram[word] = 1
            else:
                histogram[word] = histogram[word] + 1

        sorted_values = []
        sorted_values=sorted(histogram.values(), reverse=True)
        print("DEBUGGING>> ... Printing the sorted histogram....")
        print(sorted_values)
        final_dict=dict()
        for sorted_value in sorted_values:
            print("\tDebugging>> In Outer Loop")
            for word, count in histogram.items():
                print("\t\t\tDebugging>> In Inner Loop")
                print(f"Sorted Value is {sorted_value}; Word is {word}; Count is {count}")

                if count == sorted_value and count in final_dict:
                    final_dict[count] = final_dict[count].append(word)
                elif count == sorted_value and count not in final_dict:
                    final_dict[count] = [ word ]
                
                print(f"Final Dict is {final_dict}")
            
            print("\t\t\tDebugging>> Ending Inner Loop")
            print(f"Final Dict is {final_dict}")
        
        print("\tDebugging>> Ending Outer Loop")
        output_list = list(final_dict.values())
        return output_list[0: k]

    
sol = Solution()
out_list = sol.topKFrequent(['input', 'input1', 'input1', 'input2', 'input2', 'input2'], 2)
print("Printing output...")
print(out_list)