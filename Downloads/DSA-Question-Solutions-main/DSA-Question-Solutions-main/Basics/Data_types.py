LINK =" https://www.geeksforgeeks.org/problems/data-type-1666706751/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=data-type"

class Solution:
    def dataTypeSize(self, str):
        data_type ={
            "Character":"1",
            "Integer":"4",
            "Long":"8",
            "Float":"4",
            "Double":"8"
        }
        return data_type[str]

