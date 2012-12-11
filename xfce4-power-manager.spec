%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A power manager for Xfce
Name:		xfce4-power-manager
Version:	1.2.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfconf-devel >= 4.10.0
BuildRequires:	dbus-glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	intltool
BuildRequires:	libxfce4-panel-devel >= 4.10.0
BuildRequires:	polkit-1-devel
BuildRequires:	libxfce4ui-devel >= 4.10.0
Requires:	pm-utils
Requires:	hibernate
Requires:	suspend-s2ram
Requires:	upower
Conflicts:	mandriva-xfce-config-common < 2009.1-2
Requires(pre):	xfconf

%description
A power manager dedicated for Xfce desktop environment.

%prep
%setup -q

%build
%configure2_5x \
	--enable-dpms \
	--enable-panel-plugins \
	--enable-network-manager \
	--enable-polkit

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/xdg/autostart/*.desktop
%{_sbindir}/xfpm-power-backlight-helper
%{_bindir}/%{name}*
%{_bindir}/xfce4-power-information
%{_libdir}/xfce4/panel-plugins/xfce4-brightness-plugin
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_datadir}/applications/*.desktop
%{_datadir}/xfce4/doc/C/images/*.png
%{_datadir}/xfce4/doc/C/xfce4-power-manager.html
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/*


%changelog
* Sat May 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.2.0-1
+ Revision: 796426
- adjust buildrequires version
- update to new version 1.2.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.1.0-1
+ Revision: 791060
- update to new version 1.1.0

* Thu Apr 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.11-2
+ Revision: 789491
- rebuild

* Sat Mar 31 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.11-1
+ Revision: 788511
- update to new version 1.0.11
- drop patch 0

* Wed Oct 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.10-5
+ Revision: 704449
- rebuild

* Mon May 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.10-4
+ Revision: 673108
- require upower instead of devicekit-power

* Tue Apr 19 2011 Funda Wang <fwang@mandriva.org> 1:1.0.10-3
+ Revision: 656011
- build with libnotify 0.7

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 1:1.0.10-2
+ Revision: 643888
- rebuild to obsolete old packages

* Tue Feb 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.10-1
+ Revision: 639393
- update to new version 1.0.10

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.3-2
+ Revision: 633057
- rebuild for new Xfce 4.8.0

* Fri Jan 07 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.3-1mdv2011.0
+ Revision: 629658
- update to new version 1.0.3
- drop buildrequires on hal-devel
- fix filelist

* Wed Dec 22 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.2-1mdv2011.0
+ Revision: 623886
- update to new version 1.0.2

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.1-2mdv2011.0
+ Revision: 579673
- rebuild for new xfce 4.7.0

* Tue Aug 31 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.1-1mdv2011.0
+ Revision: 574875
- update to new version 1.0.1

* Sun Aug 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.0.0-1mdv2011.0
+ Revision: 570232
- update to new version 1.0.0

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.9.98-1mdv2011.0
+ Revision: 553899
- update to new version 0.9.98

* Sat Feb 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.9.90-1mdv2010.1
+ Revision: 512413
- update to new version 0.9.90
- add buildrequires on polkit-1-devel and libxfce4ui-devel
- add requires on devicekit-power (UPower)

* Sat Nov 21 2009 Funda Wang <fwang@mandriva.org> 1:0.8.4.2-1mdv2010.1
+ Revision: 468549
- update to new version 0.8.4.2

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.4.1-1mdv2010.1
+ Revision: 462263
- update to new version 0.8.4.1

* Tue Oct 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.4-1mdv2010.0
+ Revision: 455042
- update to new version 0.8.4
- adapt to new URL schemas for Xfce sources

* Thu Aug 13 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.3.1-1mdv2010.0
+ Revision: 416221
- update to new version 0.8.3.1

* Wed Aug 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.3-1mdv2010.0
+ Revision: 409652
- update to new version 0.8.3

* Thu Jul 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.2-1mdv2010.0
+ Revision: 393945
- update to new version 0.8.2

* Wed Jul 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.1.1-1mdv2010.0
+ Revision: 393366
- update to new version 0.8.1.1

* Sat Jul 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.1-1mdv2010.0
+ Revision: 392301
- update to new version 0.8.1

* Wed Jun 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.0-1mdv2010.0
+ Revision: 384924
- update to new version 0.8.0

* Sun May 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.0-0.RC2.1mdv2010.0
+ Revision: 379206
- update to new version 0.8.0-RC2

* Fri May 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.0-0.RC1.3mdv2010.0
+ Revision: 369963
- use epoch, because there was something wrong with tags
- update to new version 0.8.0RC1

* Sat Apr 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-0.beta1.2.beta1mdv2009.1
+ Revision: 366214
- update to new version 0.8.0beta1

* Mon Apr 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-0.alpha2.1.alpha2mdv2009.1
+ Revision: 364541
- add missing buildrequires on libxfce4-panel-devel
- update to new version 0.8.0 alpha 2
- drop patch0 and source1, included and fixed upstream
- fix file list

* Thu Mar 12 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.4-3mdv2009.1
+ Revision: 354350
- conflicts with mandriva-xfce-config-common, due to file relocate between these two packages

* Thu Mar 12 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.4-2mdv2009.1
+ Revision: 354342
- Patch0: do not auto-generate autostart file (mdvbz #48708)
- move here a system wide autostart file from mandriva-xfce-config-common

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.4-1mdv2009.1
+ Revision: 349185
- fix file list
- update to new version 0.6.4

* Thu Feb 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-1mdv2009.1
+ Revision: 343017
- update to new version 0.6.2

* Fri Feb 06 2009 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 338267
- New version 0.6.1

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-2mdv2009.1
+ Revision: 334474
- rebuild
- update to new version 0.6.0

* Fri Nov 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1.RC1.0mdv2009.1
+ Revision: 300801
- bump release tag
- update to new version 0.6.0RC1

* Tue Oct 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-0.beta1.3mdv2009.1
+ Revision: 298075
- add requires on suspend-s2ram

* Tue Oct 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-0.beta1.2mdv2009.1
+ Revision: 298073
- add requires on hibernate
- fix url

* Tue Oct 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-0.beta1.1mdv2009.1
+ Revision: 298064
- add source and spec files
- Created package structure for xfce4-power-manager.

