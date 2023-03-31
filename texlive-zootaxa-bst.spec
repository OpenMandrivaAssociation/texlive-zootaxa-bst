Name:		texlive-zootaxa-bst
Version:	50619
Release:	2
Summary:	A BibTeX style for the journal Zootaxa
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zootaxa-bst
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zootaxa-bst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zootaxa-bst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a .bst reference style file for the
journal Zootaxa that publishes contributions in zoology and
classification. This is a fork of apa.bst as provided by TeX
Live since this style file resembled the most Zootaxa's own
style. Further modifications were made to the code in order to
generate in-text citations and bibliography sections
appropriately.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/zootaxa-bst
%doc %{_texmfdistdir}/doc/bibtex/zootaxa-bst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
