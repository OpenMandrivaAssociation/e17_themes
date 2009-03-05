%define name 	e17_themes
%define version 0.1
%define release %mkrel 1

Summary: 	Enlightenment DR 17 themes
Name: 		%name
Version: 	%version
Release: 	%release
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL:		http://exchange.enlightenment.org/theme/
Source0:	Natural_Yellow.edj.bz2
Source1:	bwsquared.edj.bz2
Source2:	cerium.edj.bz2
Source3:	crude.edj.bz2
Source4:	cthulhain-0.5.8.edj.bz2
Source5:	grunge.edj.bz2
Source6:	milky.edj.bz2
Source7:	nyz-0.3.edj.bz2
Source8:	simply-white-0.9.2.edj.bz2
Source9:	steampunk_0_13.edj.bz2
Source10:	edjy-b.edj.bz2
Source11:	fireball.edj.bz2
BuildRoot: 	%_tmppath/%name-buildroot
Requires:	e >= 0.16.999.050

%description
E17 theme from exchange.enlightenment.org.

%prep

%build

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE1} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE2} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE3} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE4} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE5} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE6} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE7} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE8} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE9} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE10} %buildroot/%{_datadir}/enlightenment/data/themes/
cp -av %{SOURCE11} %buildroot/%{_datadir}/enlightenment/data/themes/

pushd %buildroot/%{_datadir}/enlightenment/data/themes/
for theme in *.bz2
do
bunzip2 -fv $theme
done
popd

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/enlightenment/data/themes/*.edj
