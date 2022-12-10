class Lap:
    pakli = []


    def __init__(self, power, color, name):
        self.power=power
        self.color=color
        self.name=name
        type(self).pakli.append(self)
    

    @staticmethod
    def is_stronger(strike_with, strike_to, tromf):
        """
        strike_with = obj(lap) \n
        strike_to = obj(lap) \n
        tromf = int(1-4)
        returns True if argument1 is stronger then argument2 \n
        returns False if argument1 is weaker then argument2
        """

        if (strike_with.power > strike_to.power and strike_with.color == strike_to.color) or (strike_with.color==tromf and strike_to.color!=tromf):
            return True
        else:
            return False


    @staticmethod
    def choose_worst_card(card_list, tromf):
        """
        choose the worst card in a list of cards obj() (with tromf) \n
        returns a card obj()
        """
        if type(card_list) is list:
            if len(card_list) > 0:
                worst_card = card_list[0]
                for index in range(len(card_list)):
                    if worst_card.color == tromf and card_list[index].color == tromf: 
                        if worst_card.power > card_list[index].power:
                            worst_card = card_list[index]
                    elif worst_card.color == tromf and card_list[index].color != tromf:
                            worst_card = card_list[index]
                    elif worst_card.color != tromf and card_list[index].color != tromf:
                        if worst_card.power > card_list[index].power:
                            worst_card = card_list[index]
                return worst_card
        

    @staticmethod
    def sort_strength(list_of_objs, tromf):
        """
        sort the card objs by strength. including tromf \n
        returns sorted list \n
        supports 1d or 2d list    
        """
        
        if isinstance(list_of_objs[0], list):
            #2d list
            for inner_list_i in range(len(list_of_objs)):
                list_of_objs[inner_list_i] = sorted(list_of_objs[inner_list_i], key=lambda obj: Lap.transform_power(obj, tromf))
            return list_of_objs
        else:
            #1d list
            list_of_objs=sorted(list_of_objs, key=lambda obj: Lap.transform_power(obj, tromf))
            return list_of_objs


    @staticmethod
    def transform_power(obj, tromf):
        """
        transform tromf power to int \n
        returns int (power)
        """
        if obj.color == tromf:
            #card powers range from 7 to 14. weakest 7 + 8 = 15
            new_power = obj.power + 8
            return new_power
        else:
            return obj.power




piros_hetes=Lap(7,1,"piros hetes")
piros_nyolcas=Lap(8,1,"piros nyolcas")
piros_kilences=Lap(9,1,"piros kilences")
piros_tizes=Lap(10,1,"piros tizes")
piros_also=Lap(11,1,"piros also")
piros_felso=Lap(12,1,"piros felso")
piros_csiko=Lap(13,1,"piros csiko")
piros_asz=Lap(14,1,"piros asz")
tok_hetes=Lap(7,2,"tok hetes")
tok_nyolcas=Lap(8,2,"tok nyolcas")
tok_kilences=Lap(9,2,"tok kilences")
tok_tizes=Lap(10,2,"tok tizes")
tok_also=Lap(11,2,"tok also")
tok_felso=Lap(12,2,"tok felso")
tok_csiko=Lap(13,2,"tok csiko")
tok_asz=Lap(14,2,"tok asz")
zöld_hetes=Lap(7,3,"zold hetes")
zöld_nyolcas=Lap(8,3,"zold nyolcas")
zöld_kilences=Lap(9,3,"zold kilences")
zöld_tizes=Lap(10,3,"zold tizes")
zöld_also=Lap(11,3,"zold also")
zöld_felso=Lap(12,3,"zold felso")
zöld_csiko=Lap(13,3,"zold csiko")
zöld_asz=Lap(14,3,"zold asz")
makk_hetes=Lap(7,4,"makk hetes")
makk_nyolcas=Lap(8,4,"makk nyolcas")
makk_kilences=Lap(9,4,"makk kilences")
makk_tizes=Lap(10,4,"makk tizes")
makk_also=Lap(11,4,"makk also")
makk_felso=Lap(12,4,"makk felso")
makk_csiko=Lap(13,4,"makk csiko")
makk_asz=Lap(14,4,"makk asz")

