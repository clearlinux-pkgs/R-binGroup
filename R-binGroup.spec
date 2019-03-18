#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-binGroup
Version  : 2.2.1
Release  : 7
URL      : https://cran.r-project.org/src/contrib/binGroup_2.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/binGroup_2.2-1.tar.gz
Summary  : Evaluation and Experimental Design for Binomial Group Testing
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-Rdpack
BuildRequires : R-partitions
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n binGroup

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552719479

%install
export SOURCE_DATE_EPOCH=1552719479
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library binGroup
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library binGroup
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library binGroup
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  binGroup || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/binGroup/DESCRIPTION
/usr/lib64/R/library/binGroup/INDEX
/usr/lib64/R/library/binGroup/Meta/Rd.rds
/usr/lib64/R/library/binGroup/Meta/data.rds
/usr/lib64/R/library/binGroup/Meta/features.rds
/usr/lib64/R/library/binGroup/Meta/hsearch.rds
/usr/lib64/R/library/binGroup/Meta/links.rds
/usr/lib64/R/library/binGroup/Meta/nsInfo.rds
/usr/lib64/R/library/binGroup/Meta/package.rds
/usr/lib64/R/library/binGroup/NAMESPACE
/usr/lib64/R/library/binGroup/R/binGroup
/usr/lib64/R/library/binGroup/R/binGroup.rdb
/usr/lib64/R/library/binGroup/R/binGroup.rdx
/usr/lib64/R/library/binGroup/REFERENCES.bib
/usr/lib64/R/library/binGroup/data/Rdata.rdb
/usr/lib64/R/library/binGroup/data/Rdata.rds
/usr/lib64/R/library/binGroup/data/Rdata.rdx
/usr/lib64/R/library/binGroup/help/AnIndex
/usr/lib64/R/library/binGroup/help/aliases.rds
/usr/lib64/R/library/binGroup/help/binGroup.rdb
/usr/lib64/R/library/binGroup/help/binGroup.rdx
/usr/lib64/R/library/binGroup/help/paths.rds
/usr/lib64/R/library/binGroup/html/00Index.html
/usr/lib64/R/library/binGroup/html/R.css
