#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = []

    """
    YOUR CODE HERE
    """
    
    
    for i in range(0, length):        
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    first_ticket = hash_table_retrieve(ht, "NONE")
    
    next = first_ticket
        
    while next is not "NONE":
        print(next)
        route.append(next)
        next = hash_table_retrieve(ht, next)
        
    print(route)
    return route



        

    


#1
# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# reconstruct_trip(tickets, 3)

#2
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

reconstruct_trip(tickets, 10)

