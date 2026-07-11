%global tl_name ethiop
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	LaTeX macros and fonts for typesetting Amharic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/ethiopia/ethiop
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Ethiopian language support for the babel package, including a collection
of fonts and TeX macros for typesetting the characters of the languages
of Ethiopia, with Metafont fonts based on EthTeX's. The macros use the
Babel framework.

