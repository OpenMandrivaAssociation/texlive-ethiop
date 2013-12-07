# revision 15878
# category Package
# catalog-ctan /language/ethiopia/ethiop
# catalog-date 2007-02-14 08:57:40 +0100
# catalog-license gpl
# catalog-version 0.7
Name:		texlive-ethiop
Version:	0.7
Release:	6
Summary:	LaTeX macros and fonts for typesetting Amharic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/ethiopia/ethiop
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Ethiopian language support for the babel package, including a
collection of fonts and TeX macros for typesetting the
characters of the languages of Ethiopia, with MetaFont fonts
based on EthTeX's.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/ofm/public/ethiop/etho10.ofm
%{_texmfdistdir}/fonts/ofm/public/ethiop/ethob10.ofm
%{_texmfdistdir}/fonts/ofm/public/ethiop/ethos10.ofm
%{_texmfdistdir}/fonts/ofm/public/ethiop/ethosb10.ofm
%{_texmfdistdir}/fonts/ovf/public/ethiop/etho10.ovf
%{_texmfdistdir}/fonts/ovf/public/ethiop/ethob10.ovf
%{_texmfdistdir}/fonts/ovf/public/ethiop/ethos10.ovf
%{_texmfdistdir}/fonts/ovf/public/ethiop/ethosb10.ovf
%{_texmfdistdir}/fonts/ovp/public/ethiop/etho10.ovp
%{_texmfdistdir}/fonts/ovp/public/ethiop/ethob10.ovp
%{_texmfdistdir}/fonts/ovp/public/ethiop/ethos10.ovp
%{_texmfdistdir}/fonts/ovp/public/ethiop/ethosb10.ovp
%{_texmfdistdir}/fonts/source/public/ethiop/eth__a.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth__g.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_acce.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_b.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_c_c.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_cc.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_cc_c.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_ccc2.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_d.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_dd.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_f.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_fu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_g.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_g_a.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_gg.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_ggu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_gu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_h.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_h_a.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_h_c.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_hh.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_hu_c.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_j.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_k.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_k_a.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_kk.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_kku.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_ku.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_l.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_m.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_mrf.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_mu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_n.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_nn.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_num.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_p.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_pp.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_pu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_punc.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_q.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_q_a.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_qq.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_qqu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_qu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_r.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_s.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_s_a.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_s_c.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_ss.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_t.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_tt.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_v.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_w.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_wu.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_y.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_z.mf
%{_texmfdistdir}/fonts/source/public/ethiop/eth_z_c.mf
%{_texmfdistdir}/fonts/source/public/ethiop/etha10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/etha6.mf
%{_texmfdistdir}/fonts/source/public/ethiop/etha7.mf
%{_texmfdistdir}/fonts/source/public/ethiop/etha8.mf
%{_texmfdistdir}/fonts/source/public/ethiop/etha_cod.mf
%{_texmfdistdir}/fonts/source/public/ethiop/etha_drv.mf
%{_texmfdistdir}/fonts/source/public/ethiop/etha_lig.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab11.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab12.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab14.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab18.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab24.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab36.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethab9.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethas10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb11.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb12.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb14.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb18.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb24.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb36.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethasb9.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethatt10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethb10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethb6.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethb7.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethb8.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethb_cod.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethb_drv.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethb_lig.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb11.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb12.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb14.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb18.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb24.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb36.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbb9.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbs10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb11.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb12.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb14.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb18.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb24.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb36.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbsb9.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethbtt10.mf
%{_texmfdistdir}/fonts/source/public/ethiop/ethiomac.mf
%{_texmfdistdir}/fonts/tfm/public/ethiop/etha10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/etha6.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/etha7.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/etha8.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab11.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab12.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab14.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab18.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab24.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab36.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethab9.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethas10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb11.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb12.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb14.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb18.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb24.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb36.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethasb9.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethatt10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethb6.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethb7.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethb8.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb11.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb12.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb14.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb18.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb24.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb36.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbb9.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb11.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb12.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb14.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb18.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb24.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb36.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbsb9.tfm
%{_texmfdistdir}/fonts/tfm/public/ethiop/ethbtt10.tfm
%{_texmfdistdir}/omega/ocp/ethiop/ethospc.ocp
%{_texmfdistdir}/omega/otp/ethiop/ethospc.otp
%{_texmfdistdir}/tex/latex/ethiop/etharab.sty
%{_texmfdistdir}/tex/latex/ethiop/ethiop.ldf
%{_texmfdistdir}/tex/latex/ethiop/ethiop.sty
%{_texmfdistdir}/tex/latex/ethiop/uetha.fd
%{_texmfdistdir}/tex/latex/ethiop/uethb.fd
%{_texmfdistdir}/tex/latex/ethiop/uetho.fd
%doc %{_texmfdistdir}/doc/latex/ethiop/MANIFEST
%doc %{_texmfdistdir}/doc/latex/ethiop/README
%doc %{_texmfdistdir}/doc/latex/ethiop/codeetha.tex
%doc %{_texmfdistdir}/doc/latex/ethiop/codeethb.tex
%doc %{_texmfdistdir}/doc/latex/ethiop/ethiodoc.pdf
%doc %{_texmfdistdir}/doc/latex/ethiop/ethiodoc.tex
#- source
%doc %{_texmfdistdir}/source/latex/ethiop/ethiop.dtx
%doc %{_texmfdistdir}/source/latex/ethiop/ethiop.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts omega tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7-2
+ Revision: 751640
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7-1
+ Revision: 718378
- texlive-ethiop
- texlive-ethiop
- texlive-ethiop
- texlive-ethiop

