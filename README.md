## Admix
[![Build Status](https://travis-ci.org/stevenliuyi/admix.svg?branch=master)](https://travis-ci.org/stevenliuyi/admix)
[![PyPI version](https://badge.fury.io/py/admix.svg)](https://badge.fury.io/py/admix)

Admix is a simple tool to calculate ancestry composition (admixture proportions) from SNP raw data provided by various DNA testing vendors (such as [23andme](https://www.23andme.com/) and [AncestryDNA](https://www.ancestry.com/dna/)).

- [Admix](#admix)
  - [Installation](#installation)
    - [Install from Github](#install-from-github)
    - [Install from PyPI](#install-from-pypi)
  - [Usage](#usage)
  - [Output Example](#output-example)
  - [FAQ](#faq)
  - [Raw Data Format](#raw-data-format)
  - [Models](#models)
  - [Implementation](#implementation)

### Installation
#### Install from Github
You can use `pip` to install Admix directly from this Github repository:
```
pip install git+https://github.com/stevenliuyi/admix
```

#### Install from PyPI
You can also install Admix from [PyPI](https://pypi.python.org/pypi/admix):
```
pip install admix
```

Note that due to the size limit, the package on PyPI only contains five models (`K7b`, `K12b`, `globe13`, `world9` and `E11`). If you want all models, you could download them or just install Admix from this repository as shown above.

### Usage
Suppose that you've already had your 23andme raw data downloaded and placed in the current directory with the name `my_raw_data.txt`. Then you can perform admixture calculation by specifying the calculation model (`K7b` in this example):

```
admix -f my_raw_data.txt -v 23andme -m K7b
```

You can also set multiple models for calculation:
```
admix -f my_raw_data.txt -v 23andme -m K7b K12b
```

If no models are set, the program will apply all the available models:
```
admix -f my_raw_data.txt -v 23andme
```
You can choose the raw data format by changing the `-v` or `--vendor` parameter. The values supported are listed [here](#raw-data-format).

You may also set the `-o` or `--output` parameter to write the ancestry composition results into a file:
```
admix -f my_raw_data.txt -v 23andme -o result.txt
```

If you don't have your raw data yet, you can also test the program by using a demo 23andme data file provided by the program:
```
admix -m world9
```

Chinese users may turn on the `-z` flag so the population would be displayed in Chinese:
```
admix -z -m E11
```

Besides, you may use `--sort` flag to sort the proportions and `--ignore-zeros` flag to display non-zero proportions only.

For more help information, you could use:
```
admix -h
```

### Output Example
- **English**

Command: `admix -m K12b`

Output:
```
Gedrosia: 0.06%
Siberian: 3.71%
Northwest African: 0.00%
Southeast Asian: 33.43%
Atlantic Med: 0.07%
North European: 0.00%
South Asian: 0.00%
East African: 0.00%
Southwest Asian: 0.01%
East Asian: 62.72%
Caucasus: 0.00%
Sub Saharan: 0.00%
```
- **Chinese**

Command: `admix -m K12b -z`

Output:
```
格德罗西亚: 0.06%
西伯利亚: 3.71%
西北非: 0.00%
东南亚: 33.43%
大西洋地中海: 0.07%
北欧: 0.00%
南亚: 0.00%
东非: 0.00%
西南亚: 0.01%
东亚: 62.72%
高加索: 0.00%
撒哈拉以南非洲: 0.00%
```

### FAQ
- **Question:** *Why I got the same estimated proportion for each population?*

**Answer:** This package utilizes the optimization function [scipy.optimize.minimize](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) from the [SciPy](https://www.scipy.org) library, which has a parameter `tol` to control the tolerance for termination of the optimizer. The default tolerance is set to `1e-3` here. It works most of time, but sometimes `1e-3` is too big and causes early termination. You can manually set a smaller tolerance (say `1e-4`) to obtain correct results, although it will take longer to run the optimizer. You can do that by using the `-t` or `--tolerance` flag, for example:

```
admix -f my_raw_data.txt -t 1e-4
```

### Raw Data Format
Admix supports raw data formats from the following DNA testing vendors with `-v` or `--vendor` parameter:

| parameter value | vendor |
| --------------- | ------ |
| 23andme | [23andme](https://www.23andme.com/) |
| ancestry | [AncestryDNA](https://www.ancestry.com/dna/) |
| ftdna | [FamilyTreeDNA Family Finder](https://www.familytreedna.com/products/family-finder) |
| ftdna2 | [FamilyTreeDNA Family Finder](https://www.familytreedna.com/products/family-finder) (new format) |
| wegene | [WeGene](https://www.wegene.com/en/) |
| myheritage | [MyHeritageDNA](https://www.myheritage.com/dna) |

### Models
Admix supports many publicly available admixture models. All the calculator files are properties of their authors, and are not covered by the license of this program. Links are provided which contain more information for each model.

| model value | model name | source |
| ----- | --------- | ---- |
| `K7b` | Dodecad K7b | [Link](http://dodecad.blogspot.com/2012/01/k12b-and-k7b-calculators.html) |
| `K12b` | Dodecad K12b | [Link](http://dodecad.blogspot.com/2012/01/k12b-and-k7b-calculators.html) |
| `globe13` | Dodecad globe13 | [Link](http://dodecad.blogspot.com/2012/10/globe13-calculator.html) |
| `goble10` | Dodecad globe10 | [Link](http://dodecad.blogspot.com/2012/10/globe10-calculator.html) |
| `world9` | Dodecad world9 | [Link](http://dodecad.blogspot.com/2011/12/world9-calculator.html) |
| `Eurasia7` | Dodecad Eurasia7 | [Link](http://dodecad.blogspot.com/2011/10/eurasia7-calculator.html) |
| `Africa9` | Dodecad Africa9 | [Link](http://dodecad.blogspot.com/2011/09/africa9-calculator.html) |
| `weac2` | Dodecad weac (West Eurasian cline) 2 | [Link](http://dodecad.blogspot.com/2012/06/weac2-calculator.html) |
| `E11` | E11 | [Link](http://www.ranhaer.com/thread-32241-1-1.html) |
| `K13` | Eurogenes K13 | [Link](https://bga101.blogspot.com/2013/11/updated-eurogenes-k13-at-gedmatch.html) |
| `K36` | Eurogenes K36 | [Link](http://bga101.blogspot.com/2013/03/eurogenes-k36-at-gedmatch.html) |
| `EUtest13` | Eurogenes EUtest K13 | [Link](http://bga101.blogspot.com/2013/11/updated-eurogenes-k13-at-gedmatch.html) |
| `Jtest14` | Eurogenes Jtest K14 | [Link](http://bga101.blogspot.com/2012/09/eurogenes-ashkenazim-ancestry-test-files.html) |
| `HarappaWorld` | HarappaWorld | [Link](http://www.harappadna.org/2012/05/harappaworld-admixture/) |
| `TurkicK11` | Turkic K11 | [Link](http://www.anthrogenica.com/showthread.php?8817-Turkic-K11-Admixture-Calculator) |
| `KurdishK10` | Kurdish K10 | [Link](http://www.anthrogenica.com/showthread.php?8571-K10-Kurdish-Calculator-Version-1/page6) |
| `AncientNearEast13` | Ancient Near East K13 | [Link](http://www.anthrogenica.com/showthread.php?8193-ancient-DNA-in-the-Gedrosia-Near-East-Neolithic-K13) |
| `K7AMI` | Eurogenes K7 AMI | [Link](http://www.anthrogenica.com/showthread.php?4548-Upcoming-DIY-Eurogenes-K7-amp-K8-Calculator-amp-Oracles-for-tracking-E-Asian-amp-ASI) |
| `K8AMI` | Eurogenes K8 AMI | [Link](http://www.anthrogenica.com/showthread.php?4548-Upcoming-DIY-Eurogenes-K7-amp-K8-Calculator-amp-Oracles-for-tracking-E-Asian-amp-ASI) |
| `MDLPK27` | MDLP K27 | [Link](http://www.anthrogenica.com/showthread.php?4557-Post-MDLP-K27-Results) |
| `puntDNAL` | puntDNAL K12 Ancient World | [Link](http://www.anthrogenica.com/showthread.php?8034-PuntDNAL-K12-Ancient-World-Results) |
| `K47` | LM Genetics K47 | [Link](https://anthrogenica.com/showthread.php?12788-New-K30-K47-World-Calculator) |
| `K7M1` | Tolan K7M1 | [Link](http://gen3553.pagesperso-orange.fr/ADN/Calc.htm) |
| `K13M2` | Tolan K13M2 | [Link](http://gen3553.pagesperso-orange.fr/ADN/Calc.htm) |
| `K14M1` | Tolan K14M1 | [Link](http://gen3553.pagesperso-orange.fr/ADN/Calc.htm) |
| `K18M4` | Tolan K18M4 | [Link](http://gen3553.pagesperso-orange.fr/ADN/Calc.htm) |
| `K25R1` | Tolan K25R1 | [Link](http://gen3553.pagesperso-orange.fr/ADN/Calc.htm) |
| `MichalK25`| Michal World K25 | [Link](https://anthrogenica.com/showthread.php?13359-Michal-s-World-K25-calculator) |

### Implementation
Maximum likelihood estimation (MLE) algorithm is applied for ancestry composition calculation, and the implementation is fairly straightforward.

Let $F_{nk}$ be the minor allele frequency of SNP marker $n$ for population $k$ ,
$l_n^{minor}$ and $l_n^{major}$ be the minor and major allele for marker $n$ respectively,
and $G_{ni}$ be the allele at marker $n$ of the individual we're interested in ( $i=1,2$ ).

Our goal is to find the admixture fraction $q_k$ of the individual, which maximize the log likelihood function

$$\chi_{{l^{minor}_n}}(G_{ni})j_i\log(F_{nk}q_k)+\chi_{{l^{major}_n}}(G_{ni})j_i\log((J_{nk}-F_{nk})q_k)$$

where $\chi$ is the indicator function, $J$ and $j$ are the all-ones matrix/vector. Note that the Einstein summation convention is implied here. With the constraints $0 \leq q_k \leq 1$ and $\sum {q_k} = 1$, we can obtain the admixture proportions $q_k$ by applying optimization techniques.
