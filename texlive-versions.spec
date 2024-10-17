Name:		texlive-versions
Version:	21921
Release:	2
Summary:	Optionally omit pieces of text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/versions
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/versions.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/versions.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Stephan Bellantoni's version has provided preamble commands for
selecting environments to be included/excluded. This package
does the same, but corrects, improves, and extends it in both
implementation and function.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/versions/versions.sty
%doc %{_texmfdistdir}/doc/latex/versions/versions-doc.pdf
%doc %{_texmfdistdir}/doc/latex/versions/versions-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
