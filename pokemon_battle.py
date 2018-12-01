enemy = input('Choose the pokemon you want to battle against! (Charmander) / (Bulbasaur) / (Squirtle)\n')

pikachu_hp = 35
pikachu_attack = 55
pikachu_defense = 40
pikachu_speed = 90
enemy_hp = 0
enemy_attack = 0
enemy_attack_movement = "None"
enemy_attack_movement_damage = 0
enemy_defense = 0
enemy_speed = 0
chosen_attack_damage = 0
damage = 0

if enemy == "Charmander":
    enemy_hp = 39
    enemy_attack = 52
    enemy_attack_movement = "Scratch"
    enemy_attack_movement_damage = 21
    enemy_defense = 43
    enemy_speed = 65
elif enemy == "Bulbasaur":
    enemy_hp = 45
    enemy_attack = 49
    enemy_attack_movement = "Tackle"
    enemy_attack_movement_damage = 20
    enemy_defense = 65
    enemy_speed = 45
elif enemy == "Squirtle":
    enemy_hp = 44
    enemy_attack = 48
    enemy_attack_movement = "Tackle"
    enemy_attack_movement_damage = 19
    enemy_defense = 49
    enemy_speed = 43

while pikachu_hp > 0 or enemy_hp > 0:
    chosen_atack = input("Choose the movement: (Quick attack / Thunder shock)\n")

    if chosen_atack == "Quick attack":
        chosen_attack_damage = 22
        if pikachu_speed > enemy_speed:
            damage = int(chosen_attack_damage * enemy_defense / (200 - pikachu_attack))
            enemy_hp -= damage
            if damage > enemy_hp:
                enemy_hp = 0
            print("Pikachu used Quick attack!")
            print("Enemy {} has {} hp points!".format(enemy, enemy_hp))
            if enemy_hp <= 0:
                print("Enemy {} fainted".format(enemy))
                print("The battle has finished.")
                break
            pikachu_hp -= int(enemy_attack_movement_damage * pikachu_defense / (200 - enemy_attack))
            print("Enemy {} used {}!".format(enemy, enemy_attack_movement))
            print("Pikachu has {} hp points!\n".format(pikachu_hp))
        else:
            pikachu_hp -= int(enemy_attack_movement_damage * pikachu_defense / (200 - enemy_attack))
            if enemy_attack_movement_damage > pikachu_hp:
                pikachu_hp = 0
            print("Enemy {} used {}!".format(enemy, enemy_attack_movement))
            print("Pikachu has {} hp points!".format(pikachu_hp))
            if enemy_hp <= 0:
                print("Enemy {} fainted".format(enemy))
                print("The battle has finished.")
                break
            damage = int(chosen_attack_damage * enemy_defense / (200 - pikachu_attack))
            enemy_hp -= damage
            print("Pikachu used Quick attack!")
            print("Enemy {} has {} hp points!\n".format(enemy, enemy_hp))

    elif chosen_atack == "Thunder shock":
        chosen_attack_damage = 27
        if pikachu_speed > enemy_speed:
            damage = int(chosen_attack_damage * enemy_defense / (200 - pikachu_attack))
            enemy_hp -= damage
            if damage > enemy_hp:
                    enemy_hp = 0
            print("Pikachu used Thunder shock!")
            print("Enemy {} has {} hp points!".format(enemy, enemy_hp))
            if enemy_hp <= 0:
                print("Enemy {} fainted".format(enemy))
                print("The battle has finished.")
                break
            pikachu_hp -= int(enemy_attack_movement_damage * pikachu_defense / (200 - enemy_attack))
            print("Enemy {} used {}!".format(enemy, enemy_attack_movement))
            print("Pikachu has {} hp points!\n".format(pikachu_hp))
        else:
            pikachu_hp -= int(enemy_attack_movement_damage * pikachu_defense / (200 - enemy_attack))
            if enemy_attack_movement_damage > pikachu_hp:
                pikachu_hp = 0
            print("Enemy {} used {}!".format(enemy, enemy_attack_movement))
            print("Pikachu has {} hp points!".format(pikachu_hp))
            if enemy_hp <= 0:
                print("Enemy {} fainted".format(enemy))
                print("The battle has finished.")
                break
            damage = int(chosen_attack_damage * enemy_defense / 145)
            enemy_hp -= damage
            print("Pikachu used Thunder shock!")
            print("Enemy {} has {} hp points!\n".format(enemy, enemy_hp))

