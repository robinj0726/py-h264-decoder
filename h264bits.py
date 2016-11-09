class H264Bits:

    def __init__(self, bits):
        self.bits = bits[32:]

    def u(self,n):
        return self.bits.read(n).uint

    def f(self,n):
        return self.u(n)

    def exp_golomb(self):
        zeros = 0
        while self.bits.read(1).uint == 0:
            zeros += 1
        return 0 if zeros == 0 else 2**zeros - 1 + self.bits.read(zeros).uint

    def ue(self):
        return self.exp_golomb()

    def se(self):
        from math import ceil
        k = self.exp_golomb()
        return (-1)**(k+1) * ceil(k/2)

    def ae(self):
        print("ae() not IMPL yet")
        assert False

    def more_data(self):
        return self.bits.pos < self.bits.length

    def byte_aligned(self):
        return self.bits.pos % 8 == 0


if __name__ == "__main__":
    from bitstring import BitStream
    raw = BitStream("0b110010000100")
    bs = H264Bits(raw)
    print(bs.u(1))
    print(bs.f(1))
    print(bs.ue())
    print(bs.se())
