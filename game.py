import random


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Character):
    """플레이어 클래스"""

    def __init__(self, name, hp, power, mp, magic_power):
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power
        super().__init__(name, hp, power)

    def magic_attack(self, other):  # 요구사항 4. 플레이어는 공격 타입을 선택할 수 있어야 합니다. ex) 일반공격 , 마법공격
        # 요구사항 7. 모든 공격은 캐릭터의 파워 기준으로 랜덤성을 가지고있어야 합니다. ex) 파워가 10인경우 일반공격은 8~12사이의 랜덤한 값으로 공격
        damage = random.randint(self.magic_power - 2, self.magic_power + 2)
        other.hp = max(other.hp - damage, 0)
        # 마법공격의 경우 mp가 self.magic_power + 2 보다 작으면 마법공격 불가. mp가 0보다 작아지지 않는다.
        self.mp = self.mp - damage
        print(f"{self.name}님의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

        if self.mp < self.magic_power + 2:
            print(f"더 이상 마법공격을 할 수 없습니다.\n")

    # 부모 클래스에서 self의 상태만 print하던 show_status를 self와 other 모두 출력하도록 overriding.
    # 요구사항 6. 매 전투시 플레이어와 몬스터의 상태 정보를 출력해야 합니다.
    def show_status(self, other):
        print(
            f"{self.name}님의 상태: [HP {self.hp}/{self.max_hp}]  [MP {self.mp}/{self.max_mp}]")
        print(f"{other.name}의 상태: HP {other.hp}/{other.max_hp}\n")


# 몬스터 클래스

class ElectricMonster(Character):
    def __init__(self, name, hp, power):
        self.attribute = "electric"
        super().__init__(name, hp, power)

    def show_status(self, other):  # 요구사항 6. 다른 속성의 몬스터들도 모두 같음.
        print(
            f"{other.name}님의 상태: [HP {other.hp}/{other.max_hp}]  [MP {other.mp}/{other.max_mp}]")
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n")


class FireMonster(Character):
    def __init__(self, name, hp, power):
        self.attribute = "fire"
        super().__init__(name, hp, power)

    def show_status(self, other):
        print(
            f"{other.name}님의 상태: [HP {other.hp}/{other.max_hp}]  [MP {other.mp}/{other.max_mp}]")
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n")


class WaterMonster(Character):
    def __init__(self, name, hp, power):
        self.attribute = "water"
        super().__init__(name, hp, power)

    def show_status(self, other):
        print(
            f"{other.name}님의 상태: [HP {other.hp}/{other.max_hp}]  [MP {other.mp}/{other.max_mp}]")
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n")


class GrassMonster(Character):
    def __init__(self, name, hp, power):
        self.attribute = "grass"
        super().__init__(name, hp, power)

    def show_status(self, other):
        print(
            f"{other.name}님의 상태: [HP {other.hp}/{other.max_hp}]  [MP {other.mp}/{other.max_mp}]")
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n")


# 요구사항 1. 이름을 입력해 플레이어를 생성할 수 있어야 합니다.

player_name = input("이름을 입력해 주세요: ")
print()

if not player_name:
    player_name = "Player"  # 사용자가 이름을 입력하지 않으면 default값으로 "Player"를 사용한다.

player = Player(hp=100, power=10, name=player_name, mp=70, magic_power=17)


# 요구사항 2. 몬스터는 임의 생성할 수 있어야 합니다.

random_monster_index = random.randint(0, 3)

if (random_monster_index == 0):
    random_monster = ElectricMonster(hp=100, power=11, name="Pikachu")

elif (random_monster_index == 1):
    random_monster = FireMonster(hp=80, power=12, name="Charmander")

elif (random_monster_index == 2):
    random_monster = WaterMonster(hp=150, power=7, name="Squirtle")

elif (random_monster_index == 3):
    random_monster = GrassMonster(hp=120, power=10, name="Bulbasaur")


print(f'{random_monster.attribute} 속성의 몬스터가 나타났습니다!\n')


# 요구사항 3. while 반복문을 사용해 종료 조건을 충족할 때까지 턴제 플레이어와 몬스터간 전투를 반복 진행해야 합니다.

while True:

    if player.mp >= player.magic_power+2:

        # 요구사항 4. 플레이어는 공격 타입을 선택할 수 있어야 합니다. ex) 일반공격 , 마법공격
        print(f"{player_name}님이 공격합니다.")
        print("1. 일반공격")
        print("2. 마법공격\n")

        while True:
            attack_type = input("공격 유형의 번호를 입력해 주세요: ")
            print()

            if attack_type == "1":
                player.attack(random_monster)
                # 요구사항 6. 매 전투시 플레이어와 몬스터의 상태 정보를 출력해야 합니다.
                player.show_status(random_monster)
                break
            elif attack_type == "2":
                player.magic_attack(random_monster)
                player.show_status(random_monster)
                break
            else:
                print('1과 2 중 선택하여 입력해 주세요.')
                print()

        if random_monster.hp == 0:
            # 요구사항 8. 몬스터나 플레이어의 HP가 0이되면 전투를 종료하고 승리 또는 패배를 출력해야 합니다.
            print('승리')
            break

    else:
        player.attack(random_monster)
        player.show_status(random_monster)

        if random_monster.hp == 0:
            print('승리')  # 요구사항 8.
            break

    random_monster.attack(player)  # 요구사항 5. 몬스터는 일반 공격을 할 수 있어야 합니다.
    random_monster.show_status(player)

    if player.hp == 0:
        print('패배')  # 요구사항 8.
        break

print("게임을 종료합니다.")
