# revision 21921
# category Package
# catalog-ctan /macros/latex/contrib/versions
# catalog-date 2011-04-02 19:40:46 +0200
# catalog-license lppl1.3
# catalog-version 0.55
Name:		texlive-versions
Version:	0.55
Release:	3
Summary:	Optionally omit pieces of text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/versions
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/versions.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/versions.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.55-2
+ Revision: 757420
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.55-1
+ Revision: 719887
- texlive-versions
- texlive-versions
- texlive-versions

