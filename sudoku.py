import sys

BLANK = 0
ONES = 0x3fe  # Binary 1111111110

Entry = [BLANK] * 81
Block = [ONES] * 9
Row = [ONES] * 9
Col = [ONES] * 9

InBlock = [0] * 81
InRow = [0] * 81
InCol = [0] * 81

SeqPtr = 0
Sequence = [0] * 81

Count = 0
LevelCount = [0] * 81


def swap_seq_entries(S1, S2):
    Sequence[S1], Sequence[S2] = Sequence[S2], Sequence[S1]


def init_entry(i, j, val):
    Square = 9 * i + j
    valbit = 1 << val

    Entry[Square] = valbit
    Block[InBlock[Square]] &= ~valbit
    Col[InCol[Square]] &= ~valbit
    Row[InRow[Square]] &= ~valbit

    SeqPtr2 = SeqPtr
    while SeqPtr2 < 81 and Sequence[SeqPtr2] != Square:
        SeqPtr2 += 1

    swap_seq_entries(SeqPtr, SeqPtr2)
    globals()['SeqPtr'] += 1


def print_array():
    Square = 0

    for i in range(9):
        if i % 3 == 0:
            print()
        for j in range(9):
            if j % 3 == 0:
                print(' ', end='')
            valbit = Entry[Square]
            if valbit == 0:
                ch = '-'
            else:
                for val in range(1, 10):
                    if valbit == (1 << val):
                        ch = str(val)
                        break
            print(ch, end='')
            Square += 1
        print()


def console_input():
    for i in range(9):
        print("Row[{}] : ".format(i + 1), end='')
        InputString = input()

        for j in range(9):
            ch = InputString[j]
            if ch.isdigit():
                init_entry(i, j, int(ch))


def print_stats():
    print("\nLevel Counts:\n")
    S = 0
    while LevelCount[S] == 0:
        S += 1

    i = 0
    while S < 81:
        Seq = Sequence[S]
        print("({}, {}):{:4d} ".format(Seq // 9 + 1, Seq % 9 + 1, LevelCount[S]), end='')
        if i > 4:
            print()
            i = 0
        i += 1
        S += 1

    print("\n\nCount = {}".format(Count))


def succeed():
    print_array()
    print_stats()


def next_seq(S):
    MinBitCount = 100
    S2 = S
    for T in range(S, 81):
        Square = Sequence[T]
        Possibles = Block[InBlock[Square]] & Row[InRow[Square]] & Col[InCol[Square]]
        BitCount = 0
        while Possibles:
            Possibles &= ~(Possibles & -Possibles)
            BitCount += 1

        if BitCount < MinBitCount:
            MinBitCount = BitCount
            S2 = T

    return S2


def place(S):
    # move the if ahead
    if S >= 81:
        succeed()
        return
    
    LevelCount[S] += 1
    globals()['Count'] += 1

    S2 = next_seq(S)
    swap_seq_entries(S, S2)

    Square = Sequence[S]
    BlockIndex = InBlock[Square]
    RowIndex = InRow[Square]
    ColIndex = InCol[Square]

    Possibles = Block[BlockIndex] & Row[RowIndex] & Col[ColIndex]
    while Possibles:
        valbit = Possibles & (-Possibles)
        Possibles &= ~valbit
        Entry[Square] = valbit
        Block[BlockIndex] &= ~valbit
        Row[RowIndex] &= ~valbit
        Col[ColIndex] &= ~valbit

        place(S + 1)

        Entry[Square] = BLANK
        Block[BlockIndex] |= valbit
        Row[RowIndex] |= valbit
        Col[ColIndex] |= valbit

    swap_seq_entries(S, S2)


def main():
    for i in range(9):
        for j in range(9):
            Square = 9 * i + j
            InRow[Square] = i
            InCol[Square] = j
            InBlock[Square] = (i // 3) * 3 + (j // 3)

    for Square in range(81):
        Sequence[Square] = Square
        LevelCount[Square] = 0

    console_input()
    place(SeqPtr)
    print("\n\nTotal Count = {}".format(Count))


if __name__ == "__main__":
    main()
