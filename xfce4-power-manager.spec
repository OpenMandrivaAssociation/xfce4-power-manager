Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	0.6.4
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://goodies.xfce.org/releases/xfce4-power-manager/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		xfce4-power-manager-0.6.4-dont-generate-autostart-file.patch
BuildRequires:	xfconf-devel
BuildRequires:	hal-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	intltool
BuildRequires:	libxfcegui4-devel
Requires:	pm-utils
Requires:	hibernate
Requires:	suspend-s2ram
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A power manager dedicated for Xfce desktop environment.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--enable-dpms \
	--enable-libnotify

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cp -f %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_bindir}/%{name}*
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_datadir}/xfce4/doc/C/images/*.png
%{_datadir}/xfce4/doc/C/xfce4-power-manager.html
