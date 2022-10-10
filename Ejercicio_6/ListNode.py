from typing import Any, Union

class ListNode:
    
    def __init__(self, element : Any) -> None:
        self.element = element
        self.next = None
        self.prev = None