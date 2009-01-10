%define svn     908622
%define oname   panelspacer
Summary:	    Add blank space and/or a separator line in panels
Name:		    plasma-applet-%oname
Version: 	    0.0
Release: 	    %mkrel 1.%svn.1
Source0:        %oname-%version.%svn.tar.bz2	
License: 	    GPLv2+
Group: 		    Graphical desktop/KDE
Url: 	        http://www.kde.org
BuildRoot: 	    %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	    kdebase4-runtime
BuildRequires: 	plasma-devel >= 4.0.70

%description 
Add blank space and/or a separator line in panels

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_panelspacer.so
%_kde_datadir/kde4/services/plasma-applet-panelspacer.desktop
%_kde_appsdir/desktoptheme/default/widgets/panelspacer-separator.svgz

#--------------------------------------------------------------------

%prep
%setup -q -n %oname

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
%{makeinstall_std}
cd -

%clean
rm -rf %{buildroot}
