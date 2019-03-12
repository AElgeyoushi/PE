#include <iostream>;

using namespace std;

uint64_t Trianglur(uint64_t n) {
	return n * (n + 1) / 2;
}

uint64_t Pentagonal(uint64_t n) {
	return n * (3 * n - 1) / 2;
}

uint64_t Hexagonal(uint64_t n) {
	return n * (2 * n - 1);
}

int main(int argCount, char *argValues[]) {
	uint64_t tn, pn, hn;
	uint64_t ti = 286, pi = 166, hi = 144;
	tn = Trianglur(ti);
	pn = Pentagonal(pi);
	hn = Hexagonal(hi);

	while (tn != pn || tn != hn || pn != hn) {
		if (tn <= pn && tn <= hn) {
			ti++;
			tn = Trianglur(ti);
		}
		else if (pn <= tn && pn <= hn) {
			pi++;
			pn = Pentagonal(pi);
		}
		else if (hn <= tn && hn <= pn) {
			hi++;
			hn = Hexagonal(hi);
		}
	}
	printf("%lld, %lld, %lld\n", tn, pn, hn);
	printf("\nPress any key to continue...\n");
	cin.get();
}