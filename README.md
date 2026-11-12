# Number Theory and Cryptography Workshop

**Student Name:** Apurba Chandra Roy  
**Student ID:** IT23031  
**Department:** ICT  
**University:** Mawlana Bhashani Science and Technology University (MBSTU)

---

## 1. Overview

This repository contains my coursework and Python implementations for introductory Number Theory and Cryptography. It is organized around the learning areas and practical assignments in the [official workshop repository](https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop).

> This is an independent student submission. The official workshop materials are used as references; explanations and implementations in this repository should be reviewed, run, and completed by the student before submission.

## 2. Learning objectives

- Understand divisibility, prime numbers, greatest common divisors, and modular arithmetic.
- Implement fundamental number-theoretic algorithms in Python.
- Explore modular exponentiation and Euler's totient function.
- Understand the mathematical foundations of RSA.
- Document algorithms with equations, code, outputs, and figures.

## 3. Repository structure

```text
.
├── README.md
├── notebooks/
│   ├── 01_Number_Theory_Fundamentals.ipynb
│   └── 02_RSA_Cryptography.ipynb
├── src/
│   └── number_theory.py
├── figures/
└── references/
    └── resources.md
```

## 4. Number Theory

### 4.1 Prime numbers

An integer \(p > 1\) is prime if its only positive divisors are 1 and \(p\).

```python
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True

print(is_prime(17))  # True
```

### 4.2 Greatest common divisor (Euclidean algorithm)

For integers \(a \ge b > 0\),

\[
\gcd(a,b)=\gcd(b, a \bmod b)
\]

The algorithm repeatedly replaces the pair \((a,b)\) with \((b,a\bmod b)\) until the second value is zero.

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

print(gcd(48, 18))  # 6
```

### 4.3 Modular arithmetic

For \(n>0\), the remainder \(r\) when \(a\) is divided by \(n\) satisfies

\[
a = qn + r,\qquad 0 \le r < n.
\]

```python
print(17 % 5)  # 2
```

### 4.4 Modular exponentiation

Modular exponentiation computes \(a^e \bmod m\). Python's three-argument `pow` performs this efficiently.

\[
a^e \pmod m
\]

```python
print(pow(2, 5, 7))  # 4
```

### 4.5 Euler's totient function

Euler's totient \(\varphi(n)\) counts the positive integers from 1 through \(n\) that are coprime to \(n\).

\[
\varphi(n)=|\{k:1\le k\le n,\ \gcd(k,n)=1\}|
\]

```python
def euler_totient(n: int) -> int:
    if n < 1:
        raise ValueError("n must be a positive integer")
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

print(euler_totient(9))  # 6
```

## 5. Cryptography: RSA overview

RSA is a public-key cryptosystem based on modular arithmetic and the difficulty of factoring a large composite integer.

For two distinct primes \(p,q\):

\[
n=pq,\qquad \varphi(n)=(p-1)(q-1)
\]

Choose \(e\) such that \(\gcd(e,\varphi(n))=1\), then find \(d\) satisfying

\[
ed\equiv 1\pmod{\varphi(n)}.
\]

Encryption and decryption of a message integer \(m\) are

\[
c\equiv m^e\pmod n,\qquad m\equiv c^d\pmod n.
\]

The small-number demonstration in the notebook is educational only. It is **not secure for real-world use**. Real systems require vetted cryptographic libraries and secure padding.

## 6. Practical work and results

Run the notebooks in order. Record the actual outputs from your own runs and add screenshots/figures where required by the instructor.

| Notebook | Coverage | Status |
|---|---|---|
| `01_Number_Theory_Fundamentals.ipynb` | Prime test, GCD, modular arithmetic, modular exponentiation, totient | Starter notebook |
| `02_RSA_Cryptography.ipynb` | Toy RSA key generation, encryption, decryption | Starter notebook |

## 7. References

- [Official Number Theory and Cryptography Workshop](https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop)
- [Python documentation: `math`](https://docs.python.org/3/library/math.html)
- [Python documentation: built-in `pow`](https://docs.python.org/3/library/functions.html#pow)

## 8. Academic integrity and completion checklist

- [ ] Read the official workshop README, slides, and assignment notebooks.
- [ ] Complete the official Day 1 and Day 2 fill-in-the-blank assignments.
- [ ] Run every notebook from top to bottom and verify outputs.
- [ ] Add required figures and explanations based on the actual workshop materials.
- [ ] Check that the final repository reflects your own understanding and work.
