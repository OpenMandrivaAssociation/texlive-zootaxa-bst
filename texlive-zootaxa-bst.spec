%global tl_name zootaxa-bst
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A BibTeX style for the journal Zootaxa
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/zootaxa-bst
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zootaxa-bst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zootaxa-bst.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a .bst reference style file for the journal
Zootaxa that publishes contributions in zoology and classification. This
is a fork of apa.bst as provided by TeX Live since this style file
resembled the most Zootaxa's own style. Further modifications were made
to the code in order to generate in-text citations and bibliography
sections appropriately.

