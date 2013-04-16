%define name 	e17_themes
%define version 0.2
%define release: 2

Summary: 	Enlightenment DR 17 themes
Name: 		%name
Version: 	%version
Release: 	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL:		http://exchange.enlightenment.org/theme/
#Source0:	Natural_Yellow.edj.bz2
#Source1:	bwsquared.edj.bz2
Source2:	cerium.edj.bz2
#Source3:	crude.edj.bz2
#Source4:	cthulhain-0.5.8.edj.bz2
#Source5:	grunge.edj.bz2
Source6:	milky1.0-Beta8.edj.bz2
#Source7:	nyz-0.3.edj.bz2
Source8:	simply-white-1.0.2.edj.bz2
Source9:	steampunk_0_18.edj.bz2
Source10:	edjy-b.edj.bz2
#Source11:	fireball.edj.bz2
Source12:	A-Beautiful-Blue.edj.bz2
BuildRoot: 	%_tmppath/%name-buildroot
Requires:	e >= 0.16.999.050

%description
E17 theme from exchange.enlightenment.org.

%prep

%build

%install
mkdir -p %buildroot/%{_datadir}/enlightenment/data/themes/
#cp -av %{SOURCE1} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE2} %buildroot/%{_datadir}/enlightenment/data/themes/
#cp -av %{SOURCE3} %buildroot/%{_datadir}/enlightenment/data/themes/
#cp -av %{SOURCE4} %buildroot/%{_datadir}/enlightenment/data/themes/
#cp -av %{SOURCE5} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE6} %buildroot/%{_datadir}/enlightenment/data/themes/
#cp -av %{SOURCE7} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE8} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE9} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE10} %buildroot/%{_datadir}/enlightenment/data/themes/
#cp -av %{SOURCE11} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE12} %buildroot/%{_datadir}/enlightenment/data/themes/

pushd %buildroot/%{_datadir}/enlightenment/data/themes/
for theme in *.bz2
do
bunzip2 -fv $theme
done
popd

%clean

%files
%defattr(-,root,root)
%{_datadir}/enlightenment/data/themes/*.edj


%changelog
* Sun Jan 02 2011 Crispin Boylan <crisb@mandriva.org> 0.2-1mdv2011.0
+ Revision: 627476
- Update themes and dont install ones which dont work anymore

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2011.0
+ Revision: 617946
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.1-2mdv2010.0
+ Revision: 437220
- rebuild

* Thu Mar 05 2009 Antoine Ginies <aginies@mandriva.com> 0.1-1mdv2009.1
+ Revision: 348800
- import e17_themes


