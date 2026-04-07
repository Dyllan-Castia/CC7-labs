import math

# An isotope has half-life T.
# Return the amount of a starting mass N0
# of the isotope that remains after time t,
def compute_Nt(N0, t, T):
    return N0 * (0.5) ** (t / T)

# Return the half-life of an isotope given that
# a mass N0 decays to Nt after time t
def compute_T(N0, Nt, t):
    return t * math.log(0.5) / math.log(Nt / N0)

if __name__ == "__main__":
    choice = input()

    if choice == "N":  # Calculate amount of material
        # TODO: Read N0, t, and T from one line of input and compute Nt
        N0, t, T = input().split()
        N0 = int(N0)
        t = float(t)
        T = float(T)
        Nt = compute_Nt(N0, t, T)

        print(f"Nt = {Nt:.4f}")
    elif choice == "T":  # Calculate half-life
        # TODO: Read N0, Nt, and t from one line of input and compute T
        N0, Nt, t = input().split()
        N0 = int(N0)
        Nt = float(Nt)
        t = float(t)
        T = compute_T(N0, Nt, t)

        print(f"T = {T:.4f}")
    else:
        print("invalid choice")
