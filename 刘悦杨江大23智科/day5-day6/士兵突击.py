class Gun:

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量,初始为0
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了...")

            return

        # 发射一颗子弹
        self.bullet_count -= 1

        print("%s 发射子弹[%d]...突突突" % (self.model, self.bullet_count))


# 创建枪对象
ak47 = Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()

class Soldier:
    def __init__(self, name, gun=None):
        # 姓名
        self.name = name
        # 枪，士兵初始没有枪 None 关键字表示什么都没有
        self.gun = gun

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)
        else:
            # 2. 高喊口号
            print("冲啊...[%s]" % self.name)
            if self.gun.bullet_count <= 0:
                print("没子弹了，快换弹夹...")
                # 3. 让枪装填子弹
                self.gun.add_bullet(50)
                # 4. 让枪发射子弹
                self.gun.shoot()

xsd = Soldier("xsd",ak47)
xsd.fire()