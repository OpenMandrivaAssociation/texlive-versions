%global tl_name versions
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.55
Release:	%{tl_revision}.1
Summary:	Optionally omit pieces of text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/versions
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/versions.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/versions.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Stephan Bellantoni's version has provided preamble commands for
selecting environments to be included/excluded. This package does the
same, but corrects, improves, and extends it in both implementation and
function.

